<?php
/*
* Plugin Name: Function Backup Plugin
* Plugin URI: https://example.com/function-backup-plugin
* Description: A plugin that allows you to add, edit, or delete functions to and from a database and execute them from the website.
* Version: 3.1
* Author: Luke Wilson
* Author URI: https://example.com/luke-wilson
*/

// Include the necessary WordPress file to use get_plugin_data()
require_once(ABSPATH . 'wp-admin/includes/plugin.php');

// Register the function to create a table when the plugin is activated
register_activation_hook(__FILE__, 'backup_install');
function backup_install() {
    global $wpdb;
    $table_name = $wpdb->prefix . 'backup';
    $charset_collate = $wpdb->get_charset_collate();

    $sql = "CREATE TABLE $table_name (
        id mediumint(9) NOT NULL AUTO_INCREMENT,
        name varchar(255) NOT NULL,
        code text NOT NULL,
        plugin_version varchar(50) NOT NULL,
        PRIMARY KEY (id)
    ) $charset_collate;";

    require_once(ABSPATH . 'wp-admin/includes/upgrade.php');
    dbDelta($sql);

    if ($wpdb->last_error) {
        error_log('SQL Error: ' . $wpdb->last_error);
    }

    $backup_dir = WP_CONTENT_DIR . '/uploads/function-backups/';
    if (!file_exists($backup_dir)) {
        if (!mkdir($backup_dir, 0755, true)) {
            error_log('Error creating backup directory.');
        }
    }

    $htaccess_file = $backup_dir . '.htaccess';
    if (!file_exists($htaccess_file)) {
        file_put_contents($htaccess_file, "Deny from all\n");
    }
}

// Add a menu item in the WordPress admin panel for managing function backups
add_action('admin_menu', 'backup_menu');
function backup_menu() {
    add_menu_page(
        'Function Backup',
        'Function Backup',
        'manage_options',
        'function-backup',
        'backup_page'
    );
}

// Display the admin page
function backup_page() {
    global $wpdb;

    $editing_function = null;
    $is_editing = false;

    // Check if editing a specific function
    if (isset($_GET['edit_id'])) {
        $edit_id = intval($_GET['edit_id']);
        $editing_function = $wpdb->get_row("SELECT * FROM {$wpdb->prefix}backup WHERE id = $edit_id");
        $is_editing = true;
    }

    $table_name = $wpdb->prefix . 'backup';
    $functions = $wpdb->get_results("SELECT * FROM $table_name");

    ?>
    <div class="wrap">
        <h1>Function Backup</h1>
        <form method="post">
            <?php wp_nonce_field('backup_action', 'backup_nonce'); ?>

            <input type="text" name="name" placeholder="Function Name" value="<?php echo $is_editing ? esc_attr($editing_function->name) : ''; ?>" required /><br>

            <textarea id="function-code" name="code" rows="15" cols="150" placeholder="Enter function code here" required><?php echo $is_editing ? esc_textarea(stripslashes($editing_function->code)) : ''; ?></textarea><br>
            
            <input type="submit" name="add_function" value="Add Function" class="button button-primary" />
            <?php if ($is_editing): ?>
                <input type="submit" name="update_function" value="Update Function" class="button button-primary" />
				<input type="submit" name="cancel_update" value="Cancel Update" class="button" />
			<?php endif; ?> 
		</form>

        <?php
        // Handle form submissions
        if (isset($_POST['add_function']) && check_admin_referer('backup_action', 'backup_nonce')) {
            handle_function_submission(false);
        }

        if (isset($_POST['update_function']) && check_admin_referer('backup_action', 'backup_nonce')) {
            handle_function_submission(true);

            // Redirect after updating to reset the editing state
            wp_redirect(admin_url('admin.php?page=function-backup'));
            exit; // Make sure to exit to prevent further code execution
        }
	
		if (isset($_POST['cancel_update']) && check_admin_referer('backup_action', 'backup_nonce')) {
            // Redirect to reset the editing state
            wp_redirect(admin_url('admin.php?page=function-backup'));
            exit; // Make sure to exit to prevent further code execution
        }

        // Handle deleting a specific function
        if (isset($_POST['delete_function']) && isset($_POST['id_to_delete']) && check_admin_referer('backup_action', 'backup_nonce')) {
            $id_to_delete = intval($_POST['id_to_delete']);
            delete_function($id_to_delete);
        }

        // Display saved functions
        $functions = $wpdb->get_results("SELECT * FROM {$wpdb->prefix}backup");
        if ($functions) {
            echo '<h3>Saved Functions:</h3>';
            foreach ($functions as $function) {
                echo '<div>';
				echo '<strong>Function ID:</strong> ' . esc_html($function->id) . '<br>'; // Display the Function ID
                echo '<strong>Function Name:</strong> ' . esc_html($function->name) . '<br>';

                // Edit and Delete buttons
                ?>
                <a href="?page=function-backup&edit_id=<?php echo esc_attr($function->id); ?>" class="button">Edit</a>
                <form method="post" style="display:inline;">
                    <?php wp_nonce_field('backup_action', 'backup_nonce'); ?>
                    <input type="hidden" name="id_to_delete" value="<?php echo esc_attr($function->id); ?>" />
                    <input type="submit" name="delete_function" value="Delete" class="button button-danger" />
                </form>
                <?php
                echo '</div><hr>';
            }
        }
        ?>
    </div>
    <?php
}

// Handle add/update form submissions
function handle_function_submission($is_update) {
    global $wpdb;
    $table_name = $wpdb->prefix . 'backup';

    // Validate nonce
    if (!check_admin_referer('backup_action', 'backup_nonce')) {
        wp_die('Invalid request. Please try again.');
    }

    // Sanitize and validate inputs
    $name = sanitize_text_field($_POST['name']);
    $code = wp_kses_post($_POST['code']);

    if (empty($name) || empty($code)) {
        wp_die('All fields are required. Please fill out the form completely.');
    }

    if (!preg_match('/^[a-zA-Z_][a-zA-Z0-9_]*$/', $name)) {
        wp_die('Invalid function name. Function names must start with a letter or underscore and contain only letters, numbers, or underscores.');
    }

    // Validate PHP code
    if (!is_valid_php_code($code)) {
        wp_die('Invalid PHP code. Please fix syntax errors before submitting.');
    }

    // Add or update the function
    if ($is_update) {
        $id = intval($_GET['edit_id']);
        update_function($id, $name, $code);
        echo '<div class="updated"><p>Function updated successfully!</p></div>';
    } else {
        $plugin_data = get_plugin_data(__FILE__);
        $plugin_version = $plugin_data['Version'];

        $inserted = $wpdb->insert($table_name, [
            'name' => $name,
            'code' => $code,
            'plugin_version' => $plugin_version
        ]);

        if (false === $inserted) {
            error_log('Database Error: ' . $wpdb->last_error);
            wp_die('Failed to save the function. Check logs for details.');
        } else {
            echo '<div class="updated"><p>Function added successfully!</p></div>';
        }
    }
}

// Function to add a custom function to the backup database table
function add_to_backup($name, $code) {
    global $wpdb;

    // Table name where functions will be stored
    $table_name = $wpdb->prefix . 'backup';

    // Get the plugin version (used for tracking which version of the plugin the backup belongs to)
    $plugin_data = get_plugin_data(__FILE__);
    $plugin_version = $plugin_data['Version'];

    // Directory where function backup files will be stored
    $backup_dir = WP_CONTENT_DIR . '/uploads/function-backups/';

    // Generate a unique file name based on the function name
    $file = $backup_dir . sanitize_file_name($name) . '.php';

    // Write the function code to the backup file
    if (false === file_put_contents($file, "<?php\n" . $code . "\n")) {
        error_log("Error writing to file $file.");
        return;
    }

    // Insert the backup data into the database table
    global $wpdb;
    $inserted = $wpdb->insert($table_name, array(
        'name' => $name,   // The name of the function
        'code' => $code,   // Store the function code in the database
        'plugin_version' => $plugin_version  // The version of the plugin when the backup was made
    ));

    // Log any database errors if they occur
    if ($wpdb->last_error) {
        error_log('Database Error: ' . $wpdb->last_error);
    }
}

// Update a function in the database and files
function update_function($id, $name, $code) {
    global $wpdb;
    $table_name = $wpdb->prefix . 'backup';

    $backup_dir = WP_CONTENT_DIR . '/uploads/function-backups/';
    $file = $backup_dir . sanitize_file_name($name) . '.php';

    if (false === file_put_contents($file, "<?php\n" . $code . "\n")) {
        error_log("Error writing to file $file.");
        return;
    }

    $wpdb->update($table_name, [
        'name' => $name,
        'code' => $code
    ], ['id' => $id]);
}

// Validate PHP syntax
function is_valid_php_code($code) {
    // Ensure the code starts with `<?php` for proper execution context
    if (stripos(trim($code), '<?php') !== 0) {
        $code = "<?php\n" . $code;
    }

    // Add a syntax check wrapper to prevent actual execution
    $code = "return true; ?>\n" . $code;

    try {
        eval($code);
        return true; // No syntax errors
    } catch (ParseError $e) {
        return false; // Syntax error caught
    }
}


// Function to delete a single function by ID
function delete_function($id) {
    global $wpdb;

    // Table name where functions are stored
    $table_name = $wpdb->prefix . 'backup';

    // Retrieve the function data
    $function = $wpdb->get_row("SELECT * FROM $table_name WHERE id = $id");

    if ($function) {
        // Delete the function from the database
        $wpdb->delete($table_name, ['id' => $id]);

        // Delete the function's backup file
        $file = WP_CONTENT_DIR . "/uploads/function-backups/" . sanitize_file_name($function->name) . '.php';
        if (file_exists($file)) {
            unlink($file);
        }
    }
}

// Register the AJAX action for executing a function
add_action('wp_ajax_execute_function', 'execute_function');
add_action('wp_ajax_nopriv_execute_function', 'execute_function');
function execute_function() {
    global $wpdb;

    if (!isset($_POST['function_id'])) {
        wp_send_json_error('Function ID is required.');
    }

    $function_id = intval($_POST['function_id']);
    $data = isset($_POST['data']) ? stripslashes_deep($_POST['data']) : null;

    $table_name = $wpdb->prefix . 'backup';
    $function = $wpdb->get_row($wpdb->prepare("SELECT code FROM $table_name WHERE id = %d", $function_id));

    if ($function) {
        ob_start(); // Start output buffering
        try {
            $input_data = $data; // Make the data accessible to the evaluated function
            eval(stripslashes($function->code)); // Execute the function code
            $output = ob_get_clean(); // Get the output and clean the buffer
            wp_send_json_success($output); // Return the output as a response
        } catch (Throwable $e) {
            ob_end_clean(); // Clean the buffer if there's an error
            wp_send_json_error('Error executing function: ' . $e->getMessage());
        }
    } else {
        wp_send_json_error('Function not found.');
    }
}



// Enqueue inline JavaScript
add_action('wp_enqueue_scripts', 'backup_enqueue_inline_script');
function backup_enqueue_inline_script() {
    wp_enqueue_script('jquery');

    $inline_script = <<<EOD
    jQuery(document).ready(function($) {
        $(document).on('click', '#call-function', function() {
            var functionId = $(this).data('function-id');
            var inputData = $('#data-input').val(); // Assume data is collected from an input field

            $.ajax({
                url: backupAjax.ajaxurl,
                method: 'POST',
                data: {
                    action: 'execute_function',
                    function_id: functionId,
                    data: inputData // Pass the input data
                },
                success: function(response) {
                    if (response.success) {
                        alert(response.data);
                    } else {
                        alert('Error: ' + response.data);
                    }
                }
            });
        });
    });

    EOD;

    wp_add_inline_script('jquery', $inline_script);

    wp_localize_script('jquery', 'backupAjax', [
        'ajaxurl' => admin_url('admin-ajax.php'),
    ]);
}

// Shortcode to display the button
add_shortcode('function_button', 'backup_function_button_shortcode');
function backup_function_button_shortcode($atts) {
    $atts = shortcode_atts(['id' => 0], $atts);

    if ($atts['id'] > 0) {
        return '<button id="call-function" data-function-id="' . esc_attr($atts['id']) . '">Submit</button>';
    }

    return 'Invalid function ID.';
}
?>
