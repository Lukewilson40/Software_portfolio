using System;
using System.Drawing;
using System.Windows.Forms;

public class NumberGuessingGameForm : Form
{
    private Label lblInstruction;
    private TextBox txtGuess;
    private Button btnGuess;
    private Label lblFeedback;
    private Button btnRestart;
    private int targetNumber;
    private int attempts;
    private Random random;

    public NumberGuessingGameForm()
    {
        // Initialize the form
        this.Text = "Number Guessing Game";
        this.Size = new Size(400, 300);

        // Initialize random number generator
        random = new Random();
        ResetGame();

        // Instruction Label
        lblInstruction = new Label
        {
            Text = "Guess the number between 1 and 100:",
            Location = new Point(50, 20),
            AutoSize = true
        };
        this.Controls.Add(lblInstruction);

        // Input TextBox
        txtGuess = new TextBox
        {
            Location = new Point(50, 50),
            Width = 200
        };
        this.Controls.Add(txtGuess);

        // Guess Button
        btnGuess = new Button
        {
            Text = "Guess",
            Location = new Point(260, 50),
            AutoSize = true
        };
        btnGuess.Click += BtnGuess_Click;
        this.Controls.Add(btnGuess);

        // Feedback Label
        lblFeedback = new Label
        {
            Text = "",
            Location = new Point(50, 100),
            AutoSize = true,
            ForeColor = Color.Blue
        };
        this.Controls.Add(lblFeedback);

        // Restart Button
        btnRestart = new Button
        {
            Text = "Restart",
            Location = new Point(50, 150),
            AutoSize = true,
            Visible = false
        };
        btnRestart.Click += BtnRestart_Click;
        this.Controls.Add(btnRestart);
    }

    private void ResetGame()
    {
        targetNumber = random.Next(1, 101); // Range 1 to 100
        attempts = 0;
        lblFeedback.Text = "";
        btnRestart.Visible = false;
        txtGuess.Enabled = true;
        btnGuess.Enabled = true;
    }

    private void BtnGuess_Click(object sender, EventArgs e)
    {
        if (int.TryParse(txtGuess.Text, out int guess))
        {
            attempts++;
            if (guess < targetNumber)
            {
                lblFeedback.Text = "Too low! Try again.";
            }
            else if (guess > targetNumber)
            {
                lblFeedback.Text = "Too high! Try again.";
            }
            else
            {
                lblFeedback.Text = $"Correct! You guessed it in {attempts} attempts.";
                txtGuess.Enabled = false;
                btnGuess.Enabled = false;
                btnRestart.Visible = true;
            }
        }
        else
        {
            lblFeedback.Text = "Please enter a valid number.";
        }
        txtGuess.Clear();
    }

    private void BtnRestart_Click(object sender, EventArgs e)
    {
        ResetGame();
    }

    [STAThread]
    public static void Main()
    {
        Application.EnableVisualStyles();
        Application.Run(new NumberGuessingGameForm());
    }
}
