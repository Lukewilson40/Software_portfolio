#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

// Function declarations
void displayIntro();
void exploreTownSquare();
void exploreMansion();
void exploreClockTower();
void viewInventory();
void addItemToInventory(const string& item);
bool hasItem(const string& item);

// Global variables
bool gameRunning = true;
vector<string> inventory;

int main() {
    string choice;

    // Display introduction
    displayIntro();

    // Main game loop
    while (gameRunning) {
        cout << "\nYou are standing in the center of Elyria. Where would you like to go?\n";
        cout << "1. Town Square\n";
        cout << "2. Inventor's Mansion\n";
        cout << "3. Clock Tower\n";
        cout << "4. View Inventory\n";
        cout << "5. Exit\n";
        cout << "Choose an option (1-5): ";
        cin >> choice;

        if (choice == "1") {
            exploreTownSquare();
        } else if (choice == "2") {
            exploreMansion();
        } else if (choice == "3") {
            exploreClockTower();
        } else if (choice == "4") {
            viewInventory();
        } else if (choice == "5") {
            cout << "Thank you for playing!\n";
            gameRunning = false;
        } else {
            cout << "Invalid option. Try again.\n";
        }
    }

    return 0;
}

// Function to display the introduction text
void displayIntro() {
    cout << "Welcome to Elyria, the mysterious abandoned town trapped in time.\n";
    cout << "Your goal is to uncover the secret behind the inventor’s disappearance.\n";
}

// Function to explore the Town Square
void exploreTownSquare() {
    cout << "\nYou explore the quiet and empty town square. It's eerily still.\n";
    cout << "There's not much to see here, but the mansion and clock tower loom in the distance.\n";
}

// Function to explore the Mansion
void exploreMansion() {
    cout << "\nYou approach the mansion, its windows dark and dusty.\n";

    if (!hasItem("Old Key")) {
        cout << "You find an old rusty key lying on the ground.\n";
        addItemToInventory("Old Key");
    } else {
        cout << "You've already taken the key from here.\n";
    }
}

// Function to explore the Clock Tower
void exploreClockTower() {
    cout << "\nYou stand before the towering clock tower, its hands frozen at midnight.\n";

    string choice;
    cout << "There’s a locked door here. Do you want to try to unlock it? (yes/no): ";
    cin >> choice;

    if (choice == "yes") {
        if (hasItem("Old Key")) {
            cout << "You use the Old Key to unlock the door. The door creaks open...\n";
            cout << "Inside, you find the inventor’s secret lab. You've uncovered the truth of Elyria!\n";
            cout << "Congratulations, you win!\n";
            gameRunning = false;  // End the game
        } else {
            cout << "The door is locked, but you don’t have the right key.\n";
        }
    } else {
        cout << "You decide not to open the door.\n";
    }
}

// Function to add an item to the player's inventory
void addItemToInventory(const string& item) {
    inventory.push_back(item);
    cout << item << " added to your inventory.\n";
}

// Function to view the player's inventory
void viewInventory() {
    if (inventory.empty()) {
        cout << "Your inventory is empty.\n";
    } else {
        cout << "Your inventory contains:\n";
        for (const string& item : inventory) {
            cout << "- " << item << "\n";
        }
    }
}

// Function to check if the player has a specific item in their inventory
bool hasItem(const string& item) {
    for (const string& i : inventory) {
        if (i == item) {
            return true;
        }
    }
    return false;
}
