package ui;

import java.io.IOException;
import java.util.logging.ConsoleHandler;
import java.util.logging.FileHandler;
import java.util.logging.Handler;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.util.logging.SimpleFormatter;

/**
 * Configures the global logging settings for the application.
 * Intercepts default root logger settings to prevent debug logs from leaking into the CLI interface.
 */

//@@ heehaw1234
public class ItemTaskerLogger {

    /**
     * Sets up the global logger to route outputs to a log file instead of the console UI.
     */
    public static void setup() {
        Logger rootLogger = Logger.getLogger("");

        try {
            // Append mode is true so we don't wipe logs on every single keystroke/restart
            FileHandler fileHandler = new FileHandler("itemtasker.log", true);
            fileHandler.setFormatter(new SimpleFormatter());
            fileHandler.setLevel(Level.ALL);

            // Successfully acquired the file lock, so it is now safe to silence the console 
            for (Handler handler : rootLogger.getHandlers()) {
                if (handler instanceof ConsoleHandler) {
                    rootLogger.removeHandler(handler);
                    //handler.setLevel(Level.WARNING); // Only WARNING and SEVERE get through to the screen
                }
            }

            rootLogger.addHandler(fileHandler);
            rootLogger.setLevel(Level.ALL);
        } catch (IOException e) {
            // If file creation fails, it falls back to console logging the severe error
            rootLogger.log(Level.SEVERE, "Failed to initialize log file", e);
        }
    }
}
