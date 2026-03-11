package seedu.duke;

import SKU.SKUList;

/**
 * Main entry point for ItemTasker.
 * Initialises the data model, then runs a read-evaluate-print loop
 * until the user types {@code bye} or {@code exit}.
 */
public class Duke {

    /**
     * Application entry point.
     *
     * @param args Command-line arguments (unused).
     */
    public static void main(String[] args) {
        SKUList skuList = new SKUList();
        Ui ui = new Ui();
        CommandRunner runner = new CommandRunner(skuList);

        Ui.printWelcome();

        while (runner.isRunning()) {
            String input = ui.readInput();
            ParsedCommand cmd = Parser.parse(input);
            runner.run(cmd);
        }
    }
}
