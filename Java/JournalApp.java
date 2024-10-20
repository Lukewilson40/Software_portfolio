import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

class JournalEntry implements Serializable {
    private static final long serialVersionUID = 1L;
    private String title;
    private String content;
    private String date;

    public JournalEntry(String title, String content, String date) {
        this.title = title;
        this.content = content;
        this.date = date;
    }

    public String getTitle() {
        return title;
    }

    public String getContent() {
        return content;
    }

    public String getDate() {
        return date;
    }

    @Override
    public String toString() {
        return "Date: " + date + "\nTitle: " + title + "\nContent: " + content;
    }
}

public class JournalApp {
    private static final String FILE_NAME = "journalEntries.ser";
    private static ArrayList<JournalEntry> entries = new ArrayList<>();
    private static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        loadEntriesFromFile();

        while (true) {
            System.out.println("\nJournal Application");
            System.out.println("1. Add New Entry");
            System.out.println("2. View All Entries");
            System.out.println("3. View Entry by Title");
            System.out.println("4. Exit");
            System.out.print("Select an option: ");
            
            int choice = Integer.parseInt(scanner.nextLine());

            switch (choice) {
                case 1:
                    addNewEntry();
                    break;
                case 2:
                    viewAllEntries();
                    break;
                case 3:
                    viewEntryByTitle();
                    break;
                case 4:
                    saveEntriesToFile();
                    System.out.println("Exiting the journal. Goodbye!");
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid option, please try again.");
            }
        }
    }

    private static void addNewEntry() {
        System.out.print("Enter the title: ");
        String title = scanner.nextLine();
        
        System.out.print("Enter the date (e.g., 2024-10-19): ");
        String date = scanner.nextLine();
        
        System.out.print("Enter the content: ");
        String content = scanner.nextLine();

        JournalEntry entry = new JournalEntry(title, content, date);
        entries.add(entry);
        System.out.println("Entry added successfully!");
    }

    private static void viewAllEntries() {
        if (entries.isEmpty()) {
            System.out.println("No entries found.");
        } else {
            System.out.println("All Journal Entries:");
            for (JournalEntry entry : entries) {
                System.out.println("----------------------------");
                System.out.println(entry);
                System.out.println("----------------------------");
            }
        }
    }

    private static void viewEntryByTitle() {
        System.out.print("Enter the title of the entry to view: ");
        String title = scanner.nextLine();

        for (JournalEntry entry : entries) {
            if (entry.getTitle().equalsIgnoreCase(title)) {
                System.out.println(entry);
                return;
            }
        }
        System.out.println("No entry found with the title: " + title);
    }

    private static void saveEntriesToFile() {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(FILE_NAME))) {
            oos.writeObject(entries);
            System.out.println("Entries saved to file.");
        } catch (IOException e) {
            System.out.println("Error saving entries to file: " + e.getMessage());
        }
    }

    @SuppressWarnings("unchecked")
    private static void loadEntriesFromFile() {
        File file = new File(FILE_NAME);
        if (file.exists()) {
            try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(file))) {
                entries = (ArrayList<JournalEntry>) ois.readObject();
                System.out.println("Loaded entries from file.");
            } catch (IOException | ClassNotFoundException e) {
                System.out.println("Error loading entries from file: " + e.getMessage());
            }
        }
    }
}
