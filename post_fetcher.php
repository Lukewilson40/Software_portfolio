<?php
/**
 * Plugin Name: Post Fetcher
 * Deion: Fetches data from a Data Base and creates WordPress posts automatically with AJAX.
 * Version: 1.5.2
 * Author: Luke A. Wilson
 */

if (!defined('ABSPATH')) exit; // Prevent direct access

// Create the pick up tables on activation of the plugin
function create_roadkill_tables() {
    // Access the $wpdb object (the core database abstraction class in WordPress) to interact with the database with SQL queries
    global $wpdb;
    // Retrieves the proper database character set and collation for the WordPress database
    $charset_collate = $wpdb->get_charset_collate();

    // Includes the upgrade.php file, which contains useful functions for managing database schema updates
    require_once ABSPATH . 'wp-admin/includes/upgrade.php';

    // Roadkill full Pick Up Table
    $sql1 = "CREATE TABLE {$wpdb->prefix}roadkill_picked_up (
        id BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        date_created DATETIME NOT NULL,
        date_picked_up DATETIME NOT NULL,
        location VARCHAR(255) NOT NULL,
        PRIMARY KEY (id)
    ) $charset_collate;";
    dbDelta($sql1); // dbDelta creates table if it doesnt exist

    // Roadkill Partial Pick Up Table
    $sql2 = "CREATE TABLE {$wpdb->prefix}roadkill_partial_pick_up (
        id BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
        entry_id BIGINT(20) UNSIGNED NOT NULL,
        date_partial_pick_up DATETIME NOT NULL,
        note TEXT NOT NULL,
        PRIMARY KEY (id)
    ) $charset_collate;";
    dbDelta($sql2); // dbDelta creates table if it doesnt exist
}
// wordpress will run the function in the second parameter when the plugin is activated
register_activation_hook(__FILE__, 'create_roadkill_tables');

function roadkill_fetch_latest_entries() {
    global $wpdb;

    // Prevent caching
    header("Cache-Control: no-cache, must-revalidate");
    header("Pragma: no-cache");
    header("Expires: 0");

    $form_id = get_option('entry_post_maker_form_id', '');

    // query the database to select information submitted through the gravity forms form
    $entries = $wpdb->get_results(
        "SELECT 
            e.id, 
            e.date_created,
            em1.meta_value AS name,
            em2.meta_value AS location,
            em3.meta_value AS image
        FROM {$wpdb->prefix}gf_entry e
        LEFT JOIN {$wpdb->prefix}gf_entry_meta em1 ON em1.entry_id = e.id AND em1.meta_key = 1
        LEFT JOIN {$wpdb->prefix}gf_entry_meta em2 ON em2.entry_id = e.id AND em2.meta_key = 11
        LEFT JOIN {$wpdb->prefix}gf_entry_meta em3 ON em3.entry_id = e.id AND em3.meta_key = 4
        WHERE e.form_id = {$form_id}
        ORDER BY e.date_created DESC");

    // Ensure entries are always returned as an array
    if (!is_array($entries)) {
        $entries = [];
    }

    $data = [];
    foreach ($entries as $entry) {
        // Fetch partial pickup notes for this entry
        $notes = $wpdb->get_results($wpdb->prepare(
            "SELECT date_partial_pick_up, note FROM {$wpdb->prefix}roadkill_partial_pick_up 
            WHERE entry_id = %d ORDER BY date_partial_pick_up DESC",
            $entry->id));

        // bundle the date and note text
        $formatted_notes = [];
        foreach ($notes as $note) {
            // format the date
            $date_partial_pick_up = (new DateTime($note->date_partial_pick_up))->format('F j, Y');

            $formatted_notes[] = [
                'date' => $date_partial_pick_up,
                'note' => $note->note
            ];
        }
        // format the date
        $date_created = (new DateTime($entry->date_created))->format('F j, Y');

        // make the inputed location google maps link worthy
        $location = str_replace(' ', '', $entry->location);
        $location = str_replace('"', '', $location);
        if (!empty($location)) {
            $google_maps_url = "https://www.google.com/maps?q=" . urlencode($location);
            $google_maps_link = '<a href="' . esc_url($google_maps_url) . '" target="_blank" rel="noopener noreferrer">' . esc_html($location) . '</a>';
        }

        // get is_starred column variable for updating photo toggling
        $starred = $wpdb->get_var($wpdb->prepare(
            "SELECT is_starred FROM {$wpdb->prefix}gf_entry 
            WHERE id = %d AND form_id = %d", 
            $entry->id, $form_id));

        // create array for the data
        $data[] = [
            'id' => intval($entry->id),
            'date_created' => $date_created,
            'name' => $entry->name ?? 'Unknown',
            'location' => $google_maps_link ?? 'N/A',
            'image' => $entry->image ?? '',
            'starred' => $starred,
            'notes' => $formatted_notes // Include the notes array
        ];
    }
    // get the number of pickups
    $num_full_pickups = $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->prefix}roadkill_picked_up");
    $num_partial_pickups = $wpdb->get_var("SELECT COUNT(*) FROM {$wpdb->prefix}roadkill_partial_pick_up");
    $total_pickups = $num_full_pickups + $num_partial_pickups;

    // send JSON response with all data needed for the posts
    wp_send_json_success(['total_pickups' => intval($total_pickups), 'entries' => $data]); 
}
// allow these functions to be called via a Javascript AJAX request
add_action('wp_ajax_roadkill_fetch_latest_entries', 'roadkill_fetch_latest_entries');
// for non-authenticated/logged-in users
add_action('wp_ajax_nopriv_roadkill_fetch_latest_entries', 'roadkill_fetch_latest_entries');


// Enqueue inline JavaScript for AJAX
function roadkill_enqueue_scripts() {
    ?>
    <script type="text/javascript">
        document.addEventListener("DOMContentLoaded", function () {
            // fun the function when the page loads
            fetchLatestEntries();

            // fetches the data sent from
            async function fetchLatestEntries() { 
                let formData = new FormData();
                formData.append("action", "roadkill_fetch_latest_entries");

                try {
                    // Sends a POST request to admin-ajax.php with the FormData payload, and ensures the request isn’t cached by browsers.
                    let response = await fetch("<?php echo admin_url('admin-ajax.php'); ?>?nocache=" + new Date().getTime(), {
                        method: "POST",
                        body: formData,
                        cache: "no-store"
                    });

                    // gather data sent from roadkill_fetch_latest_entries function
                    let data = await response.json();
                    if (data.success && Array.isArray(data.data.entries)) {
                        updateUI(data.data.entries, data.data.total_pickups);
                    } else {
                        console.error("Error:", error, "Data: ", data);
                    }
                } catch (error) {
                    console.error("Error fetching latest entries:", error);
                }
            }

            function updateUI(entries, total_pickups) {
                // total pickup styling and display
                let total_pickups_Container = document.getElementById("total-pickups");
                total_pickups_Container.innerHTML = `
                <div class="roadkill-counter"   
                style="background: white; 
                            color: #204ce5; 
                            padding: 12px 20px; 
                            border-radius: 8px; 
                            font-size: 20px; 
                            font-weight: bold; 
                            margin: 20px auto; 
                            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);">
                    Total Pick ups: ${total_pickups}
                </div>`;

                let entryContainer = document.getElementById("roadkill-entries");
                entryContainer.innerHTML = ""; // Clear old content

                entries.forEach(entry => {
                    let entryElement = document.createElement("div");
                    entryElement.classList.add("roadkill-entry");
                    entryElement.id = `entry-${entry.id}`;

                    let notesHtml = entry.notes?.length
                        ? `<br><h4>Partial Pickup Notes:</h4><ul>${entry.notes.map(note => `<li><strong>${note.date}: </strong>${note.note}</li>`).join('')}</ul>`
                        : "";

                    // displays the entries in a styled post format
                    entryElement.innerHTML = `
                        <article style="background: #fff; border: 1px solid #ddd; border-radius: 8px; padding: 15px; margin: 20px 0;">
                            <h3><strong>${entry.name}</strong></h3>
                            <p><strong>Date Added: </strong> ${entry.date_created}</p>
                            <p><strong>Location:</strong> ${entry.location}</p>
                            ${entry.image ? `<img src="${entry.image}" alt="Entry Image" style="max-width: 100%; max-height: 600px;">` : ""}
                            
                            <form class="pickup-form">
                                ${entry.starred == 1 ? `
                                    <input type="file" id="fileInput-${entry.id}"><br>
                                    <button class="update_pic button" style="background-color: #00a03d; color: white;" data-id="${entry.id}">
                                        Update Photo
                                    </button>
                                    <button class="cancel_update_pic button" style="color: rgba(225, 0, 0, 0.85); background-color: white; border: 1px solid #ddd; border-radius: 8px;" data-id="${entry.id}">
                                        Cancel Update
                                    </button>
                                ` : (entry.starred == 2 ? `
                                    <button class="full-pick-up button" style="background-color: #0095eb; color: white;" data-id="${entry.id}">
                                        Full Pick Up
                                    </button>
                                    <button class="partial-pick-up button" style="background-color: #ffaa00; color: white;" data-id="${entry.id}">
                                        Partial Pick Up
                                    </button>
                                ` : `
                                    <button class="pick-up button" style="background-color: #204ce5; color: white;" data-id="${entry.id}">
                                        Report Pick Up
                                    </button>
                                `)}
                            </form>
                            <div id="status-${entry.id}"></div>
                            ${notesHtml}
                        </article>
                    `;
                    entryContainer.appendChild(entryElement);
                });
                if (entries.length === 0) {
                    entryContainer.innerHTML = "<h2>No Entries at the moment.</h2>";
                }
            }

            document.addEventListener("click", async function (event) {
                if (event.target.classList.contains("pick-up")) { // pick up button
                    let entryId = event.target.dataset.id;
                    let statusElement = document.getElementById(`status-${entryId}`);

                    if (!entryId) {
                        console.error("Entry ID is missing or undefined.");
                        return;
                    }

                    let formData = new FormData();
                    formData.append("action", "toggle_pick_up");
                    formData.append("entry_id", entryId);

                    event.target.disabled = true;
                    // statusElement.innerHTML = '<p style="color: blue;">Processing...</p>';

                    try {
                        let response = await fetch("<?php echo admin_url('admin-ajax.php'); ?>", {
                            method: "POST",
                            body: formData,
                            cache: "no-store"
                        });

                        let data = await response.json();

                        if (data.success) {
                            // statusElement.innerHTML = `<p style="color: green;">${data.data.message}</p>`;
                            fetchLatestEntries();
                        } else {
                            statusElement.innerHTML = `<p style="color: red;">${data.data.message}</p>`;
                            console.error("Error processing request in Pick-Up:", error);
                            event.target.disabled = false;
                        }
                    } catch (error) {
                        console.error("Error processing request in try in Pick-Up:", error);
                        statusElement.innerHTML = '<p style="color: red;">Error processing request.</p>';
                        event.target.disabled = false;
                    }
                }

                if (event.target.classList.contains("full-pick-up")) { // full-pick up button
                    let entryId = event.target.dataset.id;
                    let statusElement = document.getElementById(`status-${entryId}`);

                    if (!entryId) {
                        console.error("Entry ID is missing or undefined in Full Pick-Up.");
                        return;
                    }

                    let formData = new FormData();
                    formData.append("action", "roadkill_handle_pickup");
                    formData.append("entry_id", entryId);

                    event.target.disabled = true;
                    statusElement.innerHTML = '<p style="color: blue;">Processing...</p>';

                    try {
                        let response = await fetch("<?php echo admin_url('admin-ajax.php'); ?>", {
                            method: "POST",
                            body: formData,
                            cache: "no-store"
                        });

                        let data = await response.json();
                        console.log("data.data: ", data.data);

                        if (data.success) {
                            statusElement.innerHTML = `<p style="color: green;">${data.data.message}</p>`;
                            document.getElementById(`entry-${entryId}`)?.remove();
                        } else {
                            statusElement.innerHTML = `<p style="color: red;">${data.data.message}</p>`;
                            event.target.disabled = false;
                            console.error("Error processing request in Full Pick-Up:", error);
                        }
                    } catch (error) {
                        console.error("Error processing request in try in Full Pick-up:", error);
                        statusElement.innerHTML = '<p style="color: red;">Error processing request.</p>';
                        event.target.disabled = false;
                    }
                    fetchLatestEntries();
                }

                if (event.target.classList.contains("partial-pick-up")) { // partial-pickup button
                    let entryId = event.target.dataset.id;
                    let statusElement = document.getElementById(`status-${entryId}`);

                    if (!entryId) {
                        console.error("Entry ID is missing or undefined.");
                        return;
                    }

                    let formData = new FormData();
                    formData.append("action", "roadkill_handle_partial_pickup");
                    formData.append("entry_id", entryId);

                    let note = prompt("What did you pick up?");
                    if (!note) {
                        alert("Partial pickup requires a note.");
                        // revert buttons back to report pick up button
                        formData.append("update_photo", "false");
                    }
                    if (note) {
                        formData.append("note", note);

                        if (confirm("Would you like to update the photo?")) {
                            formData.append("update_photo", "true");
                        }
                        statusElement.innerHTML = '<p style="color: blue;">Processing...</p>';
                    }

                    event.target.disabled = true;

                    try {
                        let response = await fetch("<?php echo admin_url('admin-ajax.php'); ?>", {
                            method: "POST",
                            body: formData,
                            cache: "no-store"
                        });

                        let data = await response.json();

                        if (data.success) {
                            statusElement.innerHTML = `<p style="color: green;">${data.data.message}</p>`;
                            document.getElementById(`entry-${entryId}`)?.remove();
                        } else {
                            statusElement.innerHTML = `<p style="color: red;">${data.data.message}</p>`;
                            event.target.disabled = false;
                        }
                    } catch (error) {
                        console.error("Error processing request:", error);
                        statusElement.innerHTML = '<p style="color: red;">Error processing request.</p>';
                        event.target.disabled = false;
                    }
                    fetchLatestEntries();
                }

                if (event.target.classList.contains("update_pic")) { // update picture button
                    let entryId = event.target.dataset.id;
                    let statusElement = document.getElementById(`status-${entryId}`);   
                    const fileInput = document.getElementById(`fileInput-${entryId}`);

                    const file = fileInput.files[0];
                    if (!file) {
                        alert("No file selected!");
                        return;
                    }

                    let formData = new FormData();
                    formData.append("file", file);
                    formData.append("action", "roadkill_handle_file_upload");
                    formData.append("entry_id", entryId);

                    event.target.disabled = true;
                    statusElement.innerHTML = '<p style="color: blue;">Processing...</p>';

                    try {
                        let response = await fetch("<?php echo admin_url('admin-ajax.php'); ?>", {
                            method: "POST",
                            body: formData,
                            cache: "no-store"
                        });

                        let data = await response.json();

                        if (data.success) {
                            statusElement.innerHTML = `<p style="color: green;">${data.data.message}</p>`;
                            fetchLatestEntries();
                        } else {
                            statusElement.innerHTML = `<p style="color: red;">${data.data.message}</p>`;
                            event.target.disabled = false;
                        }
                    } catch (error) {
                        console.error("Error processing request:", error);
                        statusElement.innerHTML = '<p style="color: red;">Error processing request.</p>';
                        event.target.disabled = false;
                    }
                    
                }
                if (event.target.classList.contains("cancel_update_pic")) { // cancel update picture button
                    let entryId = event.target.dataset.id;
                    let statusElement = document.getElementById(`status-${entryId}`);   


                    let formData = new FormData();
                    formData.append("action", "cancel_file_upload");
                    formData.append("entry_id", entryId);

                    event.target.disabled = true;
                    statusElement.innerHTML = '<p style="color: blue;">Processing...</p>';

                    try {
                        let response = await fetch("<?php echo admin_url('admin-ajax.php'); ?>", {
                            method: "POST",
                            body: formData,
                            cache: "no-store"
                        });

                        let data = await response.json();

                        if (data.success) {
                            statusElement.innerHTML = `<p style="color: green;">${data.data.message}</p>`;
                            fetchLatestEntries();
                        } else {
                            statusElement.innerHTML = `<p style="color: red;">${data.data.message}</p>`;
                            event.target.disabled = false;
                        }
                    } catch (error) {
                        console.error("Error processing request:", error);
                        statusElement.innerHTML = '<p style="color: red;">Error processing request.</p>';
                        event.target.disabled = false;
                    }
                    
                }
                if (event.target.classList.contains("get-location")) { // get location button from gravity forms custom html
                    let formData = new FormData();
                    formData.append("action", "check_duplicate_entry");

                    try {
                        let response = await fetch("<?php echo admin_url('admin-ajax.php'); ?>", {
                            method: "POST",
                            body: formData,
                            cache: "no-store"
                        });

                        let data = await response.json();
                        if (data.success) {
                            let latest_entry = document.getElementById('input_1_11').value;
                            let duplicate_entry = false;

                            let coords = data.data;
                            for (let i = 0; i < coords.length; i++) {
                                if (getDistanceInMeters(latest_entry, coords[i].meta_value) < 3) {
                                    duplicate_entry = true;
                                };
                            }
                            if (duplicate_entry == true) {
                                alert("There is an existing entry within 3 meters of your location. You might be submitting a duplicate entry.")
                            }
                        } else {
                            console.error("Data is not success in getting location from get location field", error);
                        }
                    } catch (error) {
                        console.error("Error processing request:", error);
                    }
                }
            });
            // function for calculating the distance between 2 coordinates
            function getDistanceInMeters(coord1, coord2) {
                const toRadians = (degrees) => degrees * (Math.PI / 180);

                // 6371 km in meters. Earth’s radius
                const R = 6371e3; 

                // Parse latitude and longitude from input strings
                const [lat1, lon1] = coord1.split(',').map(Number);
                const [lat2, lon2] = coord2.split(',').map(Number);

                // Convert latitude and longitude from degrees to radians
                const φ1 = toRadians(lat1);
                const φ2 = toRadians(lat2);
                const Δφ = toRadians(lat2 - lat1);
                const Δλ = toRadians(lon2 - lon1);

                // Haversine formula
                const a = Math.sin(Δφ / 2) * Math.sin(Δφ / 2) +
                        Math.cos(φ1)     * Math.cos(φ2) *
                        Math.sin(Δλ / 2) * Math.sin(Δλ / 2);
                const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

                // Compute the distance in meters
                const distance = R * c;
                return distance.toFixed(2); // Returns distance in meters
            }

        });
    </script>
    <?php
}
add_action('wp_footer', 'roadkill_enqueue_scripts');


function toggle_pick_up() {
    global $wpdb;

    if (!isset($_POST['entry_id'])) {
        wp_send_json_error(['message' => 'Missing entry_id'], 400);
    }
    $entry_id = intval($_POST['entry_id']);

    $form_id = get_option('entry_post_maker_form_id', '');

    $starred = $wpdb->get_var($wpdb->prepare(
        "SELECT is_starred FROM {$wpdb->prefix}gf_entry 
        WHERE id = %d AND form_id = %d", 
        $entry_id, $form_id));

    // change is_starred to 2 when the pick up button is clicked
    if ($starred != 2) {
        $table_name = $wpdb->prefix . 'gf_entry';

        $wpdb->update(
            $table_name,
            ['is_starred' => 2],
            ['id' => $entry_id, 'form_id' => $form_id],
            ['%d'],
            ['%d', '%d']
        );
    }
    wp_send_json_success(['message' => 'Pickup toggled successfully!', 'entry_id' => $entry_id]);
}
add_action('wp_ajax_toggle_pick_up', 'toggle_pick_up');
add_action('wp_ajax_nopriv_toggle_pick_up', 'toggle_pick_up');


function check_duplicate_entry() {
    global $wpdb;
    $form_id = get_option('entry_post_maker_form_id', '');
    $coordinates = $wpdb->get_results($wpdb->prepare(
        "SELECT meta_value FROM {$wpdb->prefix}gf_entry_meta 
        WHERE meta_key = %s AND form_id = %d", 
        "11", $form_id));
    wp_send_json_success($coordinates); 

}
add_action('wp_ajax_check_duplicate_entry', 'check_duplicate_entry');
add_action('wp_ajax_nopriv_check_duplicate_entry', 'check_duplicate_entry');


function cancel_file_upload() {
    if (empty($_POST['entry_id'])) {
        wp_send_json_error(['message' => 'Invalid entry ID.']);
    }
    $entry_id = intval($_POST['entry_id']);
    $form_id = get_option('entry_post_maker_form_id', '');

    global $wpdb;
    $starred = $wpdb->get_var($wpdb->prepare(
        "SELECT is_starred FROM {$wpdb->prefix}gf_entry 
        WHERE id = %d AND form_id = %d", 
        $entry_id, $form_id));

    // change is_starred back to 0 when the cancel update photo button is clicked
    if ($starred != 0) {
        $table_name = $wpdb->prefix . 'gf_entry';

        $wpdb->update(
            $table_name,
            ['is_starred' => 0],
            ['id' => $entry_id, 'form_id' => $form_id],
            ['%d'],
            ['%d', '%d']
        );
    }
    wp_send_json_success(['message' => 'Canceled Photo Update Successfully!']);
}
add_action('wp_ajax_cancel_file_upload', 'cancel_file_upload');
add_action('wp_ajax_nopriv_cancel_file_upload', 'cancel_file_upload');


function roadkill_handle_file_upload() {
    if (!isset($_FILES['file']) || empty($_POST['entry_id'])) {
        wp_send_json_error(['message' => 'No file uploaded or invalid entry ID.']);
    }
    $entry_id = intval($_POST['entry_id']);
    $form_id = get_option('entry_post_maker_form_id', '');

    global $wpdb;
    $starred = $wpdb->get_var($wpdb->prepare(
        "SELECT is_starred FROM {$wpdb->prefix}gf_entry 
        WHERE id = %d AND form_id = %d", 
        $entry_id. $form_id));

    // change is_starred back to 0 when the update photo button is clicked
    if ($starred != 0) {
        $table_name = $wpdb->prefix . 'gf_entry';

        $wpdb->update(
            $table_name,
            ['is_starred' => 0],
            ['id' => $entry_id, 'form_id' => $form_id],
            ['%d'],
            ['%d', '%d']
        );
    }

    $file = $_FILES['file'];
    // Check file type
    $allowed_types = ['jpg', 'jpeg', 'png', 'gif'];
    $file_info = wp_check_filetype($file['name']);
    if (!in_array($file_info['ext'], $allowed_types)) {
        wp_send_json_error(['message' => 'Invalid file type. Only JPG, PNG, GIF are allowed.']);
    }

    // Handle file upload
    $upload = wp_handle_upload($file, ['test_form' => false]);
    if (isset($upload['error'])) {
        wp_send_json_error(['message' => 'Upload failed: ' . $upload['error']]);
    }
    $photo_path = esc_url($upload['url']);


    // Retrieve file path from database before it get updated
    $file_url = $wpdb->get_var($wpdb->prepare(
        "SELECT meta_value FROM {$wpdb->prefix}gf_entry_meta 
        WHERE meta_key = %s AND entry_id = %d AND form_id = %d", 
        "4", $entry_id, $form_id
    ));

    // Convert URL to server path
    $upload_dir = wp_upload_dir();
    $base_url = $upload_dir['baseurl'];
    $base_path = $upload_dir['basedir'];

    // Convert URL to absolute file path
    $file_path = str_replace($base_url, $base_path, $file_url);

    // delete photo's stored in the websites files
    if ($file_url) {

        // Ensure file exists before deletion
        if (file_exists($file_path)) {
            if (unlink($file_path)) {
                $message = "✅ File deleted successfully!";
            } else {
                $message = "❌ Error deleting file.";
            }
        } else {
            $message = "⚠️ File not found on the server.";
        }
    } else {
        $message = "⚠️ No file found in the database.";
    }


    // update photo in the database
    $table_name = $wpdb->prefix . 'gf_entry_meta';
    $result = $wpdb->update(
        $table_name,
        ['meta_value' => $photo_path],
        ['meta_key' => 4, 'entry_id' => $entry_id, 'form_id' => $form_id],
        ['%s'],
        ['%d', '%d', '%d']
    );
    wp_send_json_success(['message' => 'Photo updated successfully!', 'url' => $photo_path]);
}
add_action('wp_ajax_roadkill_handle_file_upload', 'roadkill_handle_file_upload');
add_action('wp_ajax_nopriv_roadkill_handle_file_upload', 'roadkill_handle_file_upload');

// Handle AJAX request for pickups
function roadkill_handle_pickup() {
    global $wpdb;
    $entry_id = intval($_POST['entry_id']);

    if (!$entry_id) {
        wp_send_json_error(['message' => 'Invalid entry ID.']);
    }
    $form_id = get_option('entry_post_maker_form_id', '');

    // get data for picked up entry
    $location = $wpdb->get_var($wpdb->prepare(
        "SELECT meta_value FROM {$wpdb->prefix}gf_entry_meta 
        WHERE meta_key = %s AND entry_id = %d AND form_id = %d", 
        "11", $entry_id, $form_id));

    $name = $wpdb->get_var($wpdb->prepare(
        "SELECT meta_value FROM {$wpdb->prefix}gf_entry_meta 
        WHERE meta_key = %s AND entry_id = %d AND form_id = %d", 
        "1", $entry_id, $form_id));

    $date = $wpdb->get_var($wpdb->prepare(
        "SELECT date_created FROM {$wpdb->prefix}gf_entry 
        WHERE id = %d AND form_id = %d", 
        $entry_id, $form_id));

    // enter data into the picked up table
    $wpdb->insert("{$wpdb->prefix}roadkill_picked_up", [
        'name' => $name,
        'date_created' => $date,
        'date_picked_up' => current_time('mysql'),
        'location' => $location
    ], ['%s', '%s', '%s', '%s']);

    // Retrieve file path from database before it get deleted
    $file_url = $wpdb->get_var($wpdb->prepare(
        "SELECT meta_value FROM {$wpdb->prefix}gf_entry_meta 
        WHERE meta_key = %s AND entry_id = %d AND form_id = %d", 
        "4", $entry_id, $form_id
    ));

    // Convert URL to server path
    $upload_dir = wp_upload_dir();
    $base_url = $upload_dir['baseurl'];
    $base_path = $upload_dir['basedir'];

    // Convert URL to absolute file path
    $file_path = str_replace($base_url, $base_path, $file_url);

    // delete photo's stored in the websites files
    if ($file_url) {

        // Ensure file exists before deletion
        if (file_exists($file_path)) {
            if (unlink($file_path)) {
                $message = "✅ File deleted successfully!";
            } else {
                $message = "❌ Error deleting file.";
            }
        } else {
            $message = "⚠️ File not found on the server.";
        }
    } else {
        $message = "⚠️ No file found in the database.";
    }

    // delete entry that was picked up from the gf tables
    $wpdb->query($wpdb->prepare(
        "DELETE FROM {$wpdb->prefix}gf_entry_meta 
        WHERE entry_id = %d AND form_id = %d", 
        $entry_id, $form_id));

    $wpdb->query($wpdb->prepare(
        "DELETE FROM {$wpdb->prefix}gf_entry 
        WHERE id = %d AND form_id = %d", 
        $entry_id, $form_id));

    // $wpdb->query($wpdb->prepare(
    // "DELETE FROM {$wpdb->prefix}roadkill_partial_pick_up 
    // WHERE entry_id = %d", 
    // $entry_id));

    wp_send_json_success(['message' => $message, 'file url' => $file_url, 'file path' => $file_path, 'entry id' => $entry_id]);
}
add_action('wp_ajax_roadkill_handle_pickup', 'roadkill_handle_pickup');
add_action('wp_ajax_nopriv_roadkill_handle_pickup', 'roadkill_handle_pickup');

function roadkill_handle_partial_pickup() {
    global $wpdb;
    $entry_id = intval($_POST['entry_id']);
    $note = sanitize_text_field($_POST['note']);
    $date_partial_pick_up = current_time('mysql');
    $update_photo = isset($_POST['update_photo']) ? $_POST['update_photo'] : false;

    if (!$entry_id) {
        wp_send_json_error(['message' => 'Invalid entry ID.']);
    }
 
    $form_id = get_option('entry_post_maker_form_id', '');

    global $wpdb;
    $table_name = $wpdb->prefix . 'gf_entry';
    if ($update_photo == "true") {
        $update_result = $wpdb->update(
            $table_name,
            ['is_starred' => 1],
            ['id' => $entry_id, 'form_id' => $form_id],
            ['%d'],
            ['%d', '%d']
        );
    } else {
        $update_result = $wpdb->update(
            $table_name,
            ['is_starred' => 0],
            ['id' => $entry_id, 'form_id' => $form_id],
            ['%d'],
            ['%d', '%d']
        );
    }

    if (!empty($note)) {
        // Insert partial pickup into the database
        $wpdb->insert("{$wpdb->prefix}roadkill_partial_pick_up", [
            'entry_id' => $entry_id,
            'date_partial_pick_up' => $date_partial_pick_up,
            'note' => $note
        ], ['%d', '%s', '%s']);
        wp_send_json_success(['message' => 'Partial Pickup recorded successfully!']);
    }

}
add_action('wp_ajax_roadkill_handle_partial_pickup', 'roadkill_handle_partial_pickup');
add_action('wp_ajax_nopriv_roadkill_handle_partial_pickup', 'roadkill_handle_partial_pickup');

// Display entries from the form
function display_custom_entries() {
    global $wpdb;
    ob_start();

    // this ⬇️ is for development and debugging use only
    // $file_count = 0;
    // $gf_dir = WP_CONTENT_DIR . "/uploads/";
    // $rii = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($gf_dir));
    // $files = [];

    // foreach ($rii as $file) {
    //     if ($file->isFile() && preg_match('/\.jpg$/i', $file->getFilename())) {
    //         $files[] = $file->getPathname();
    //     }
    // }

    // if ($files) {
    //     foreach ($files as $file) {
    //         // unlink($file);
    //         // echo "<p>Found: $file</p>";
    //         $file_count += 1;
    //     }
    // }
    // echo "<p>File Count: $file_count</p>";

    // // $f_pickups = $wpdb->query("DELETE FROM {$wpdb->prefix}roadkill_picked_up");
    // // $p_pickups = $wpdb->query("DELETE FROM {$wpdb->prefix}roadkill_partial_pick_up");

    // ob_flush();
    // flush();
    // ^ end of this snippet of development and debugging code

    ?>
    <div id="total-pickups"></div>
    <div id="roadkill-entries">
        <p>Loading entries...</p>
    </div>
    <?php

    return ob_get_clean();
}
add_shortcode('custom_entries', 'display_custom_entries');


// Add a menu item in the WordPress admin panel for managing gravity form id's
function entry_post_maker() {
    add_menu_page(
        'Entry Post Maker',     // page title
        'Entry Post Maker',     // menu title
        'manage_options',       // admin capability
        'entry-post-maker',     // menu slug
        'entry_post_maker_page' // callback function
    );
}
add_action('admin_menu', 'entry_post_maker');

function entry_post_maker_page() {
    global $wpdb;

    // Get the saved Form ID
    $saved_form_id = get_option('entry_post_maker_form_id', '');
    ?>
    <div class="wrap">
        <h1>Assign Gravity Form ID</h1>
        <form method="post">
            <label for="form-id">Gravity Form ID:</label>
            <input type="number" name="form-id" id="form-id" placeholder="Form ID" required>
            <input type="submit" name="save-form" value="Save" class="button button-primary">
        </form>
        
        <?php if ($saved_form_id): ?>
            <p>Currently assigned Form ID: <strong><?php echo esc_html($saved_form_id); ?></strong></p>
        <?php endif; ?>
    </div>
    <?php

    // Handle form submission
    if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST['save-form'])) {
        $form_id = isset($_POST['form-id']);

        if ($form_id <= 0) {
            echo '<div class="error"><p><strong>Error:</strong> Please enter a valid Form ID.</p></div>';
        } else {
            // Query the Gravity Forms table
            $form_selected = $wpdb->get_var($wpdb->prepare(
                "SELECT title FROM {$wpdb->prefix}gf_form 
                WHERE id = %d", 
                intval($form_id)));

            if ($form_selected) {
                echo '<div class="updated"><p>Is your form: <strong>' . esc_html($form_selected) . '</strong>?</p></div>';
                ?>
                <form method="post">
                    <input type="hidden" name="confirmed-form-id" value="<?php echo esc_attr($form_id); ?>">
                    <input type="submit" name="correct-form" value="Yes" class="button button-primary">
                    <a href="?page=entry-post-maker" class="button button-secondary">No</a>
                </form>
                <?php
                // return; // Stop execution to prevent the form from being displayed again
            } else {
                echo '<div class="error"><p>No form found with this ID. Please try again.</p></div>';
            }
        }
    }

    // Handle confirmation form submission
    if ($_SERVER["REQUEST_METHOD"] === "POST" && isset($_POST['correct-form'])) {
        $confirmed_form_id = isset($_POST['confirmed-form-id']) ? intval($_POST['confirmed-form-id']) : 0;
        if ($confirmed_form_id > 0) {
            update_option('entry_post_maker_form_id', $confirmed_form_id);
            echo '<div class="updated"><p>Form ID successfully saved! Form ID: <strong>' . esc_html($confirmed_form_id) . '</strong></p></div>';
        }
    }
}

