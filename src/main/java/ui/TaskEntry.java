package ui;


import skutask.SKUTask;

/** Bundles a task with its parent SKU ID and precomputed distance for sorting. */
public class TaskEntry {
    final String skuId;
    final SKUTask task;
    final int distance;

    TaskEntry(String skuId, SKUTask task, int distance) {
        this.skuId = skuId;
        this.task = task;
        this.distance = distance;
    }
}