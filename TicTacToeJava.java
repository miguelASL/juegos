package org.example;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class TicTacToeJava {
    private JFrame frame;
    private JButton[][] buttons;
    private String currentPlayer = "X";

    public TicTacToeJava() {
        frame = new JFrame("Tres en Raya");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 300);
        frame.setLayout(new GridLayout(3, 3));

        buttons = new JButton[3][3];
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                buttons[i][j] = new JButton("");
                buttons[i][j].setFont(new Font("Helvetica", Font.PLAIN, 20));
                frame.add(buttons[i][j]);
                final int row = i;
                final int col = j;
                buttons[i][j].addActionListener(new ActionListener() {
                    public void actionPerformed(ActionEvent e) {
                        onButtonClick(row, col);
                    }
                });
            }
        }

        frame.setVisible(true);
    }

    public void onButtonClick(int row, int col) {
        if (buttons[row][col].getText().equals("")) {
            buttons[row][col].setText(currentPlayer);
            buttons[row][col].setEnabled(false);
            if (checkWinner()) {
                JOptionPane.showMessageDialog(frame, currentPlayer + " ha ganado!");
                resetGame();
            } else if (isBoardFull()) {
                JOptionPane.showMessageDialog(frame, "Empate");
                resetGame();
            } else {
                currentPlayer = (currentPlayer.equals("X")) ? "O" : "X";
            }
        }
    }

    public boolean checkWinner() {
        for (int i = 0; i < 3; i++) {
            if (!buttons[i][0].getText().equals("") && buttons[i][0].getText().equals(buttons[i][1].getText()) && buttons[i][0].getText().equals(buttons[i][2].getText())) {
                return true;
            }
            if (!buttons[0][i].getText().equals("") && buttons[0][i].getText().equals(buttons[1][i].getText()) && buttons[0][i].getText().equals(buttons[2][i].getText())) {
                return true;
            }
        }
        if (!buttons[0][0].getText().equals("") && buttons[0][0].getText().equals(buttons[1][1].getText()) && buttons[0][0].getText().equals(buttons[2][2].getText())) {
            return true;
        }
        if (!buttons[0][2].getText().equals("") && buttons[0][2].getText().equals(buttons[1][1].getText()) && buttons[0][2].getText().equals(buttons[2][0].getText())) {
            return true;
        }
        return false;
    }

    public boolean isBoardFull() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (buttons[i][j].getText().equals("")) {
                    return false;
                }
            }
        }
        return true;
    }

    public void resetGame() {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                buttons[i][j].setText("");
                buttons[i][j].setEnabled(true);
            }
        }
        currentPlayer = "X";
    }
}
