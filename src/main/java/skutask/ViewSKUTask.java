package skutask;


import sku.SKU;
import sku.SKUList;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.stream.Collectors;
import java.util.Comparator;


public class ViewSKUTask {
    private String skuFilter;
    private String priorityFilter;
    private String locationFilter;

    public List<SKUTask> listTasks(SKUList fullList, HashMap<String, SKUTaskList> taskMap) {
        List<SKUTask> allTasks = new ArrayList<>();
        for (SKUTaskList taskList : taskMap.values()) {
            allTasks.addAll(taskList.getSKUTaskList());
        }

        List<SKUTask> result;

        // Handle SKU Filter: "listtasks n/SKU_ID"
        if (skuFilter != null) {
            result = allTasks.stream()
                    .filter(t -> t.getSKUTaskID().equalsIgnoreCase(skuFilter))
                    .collect(Collectors.toList());

            // Handle Priority Filter: "listtasks p/HIGH"
        } else if (priorityFilter != null) {
            return allTasks.stream()
                    .filter(t -> t.getSKUTaskPriority().toString().equalsIgnoreCase(priorityFilter))
                    .collect(Collectors.toList());

            // Handle Distance Filter: "listtasks l/B2"
        } else if (locationFilter != null) {
            result = allTasks.stream()
                    .sorted(Comparator.comparingInt(t -> calculateDistance(t, locationFilter, fullList)))
                    .collect(Collectors.toList());
        } else {
            result = allTasks;
        }
        return result;
    }

    public void setSkuFilter(String skuFilter) {
        this.skuFilter = skuFilter;
    }

    public void setPriorityFilter(String priorityFilter) {
        this.priorityFilter = priorityFilter;
    }

    public void setLocationFilter(String locationFilter) {
        this.locationFilter = locationFilter;
    }


    public int calculateDistance(SKUTask task, String currentPos, SKUList fullList) {
        SKU parentSku = null;
        for (SKU s : fullList.getSKUList()) {
            if (s.getSKUID().equals(task.getSKUTaskID())) {
                parentSku = s;
                break;
            }
        }
        if (parentSku == null) {
            return 0;
        }
        ;

        String targetName = parentSku.getSKULocation().name();
        int targetX = targetName.charAt(0) - 'A';
        int targetY = Character.getNumericValue(targetName.charAt(1)) - 1;
        int currentX = currentPos.toUpperCase().charAt(0) - 'A';
        int currentY = Character.getNumericValue(currentPos.charAt(1)) - 1;
        return Math.abs(targetX - currentX) + Math.abs(targetY - currentY);
    }
}
