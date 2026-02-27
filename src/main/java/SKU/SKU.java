package SKU;

public class SKU {
    private String skuID;
    private Location skuLocation;
    //private SKUTaskList skuTaskList;

    public SKU(String skuID, Location skuLocation) {
        this.skuID = skuID;
        this.skuLocation = skuLocation;
        // this.skuTaskList = new SKUTaskList();
    }

    public String getSKUID() {
        return skuID;
    }

    public Location getSKULocation() {
        return skuLocation;
    }
}
