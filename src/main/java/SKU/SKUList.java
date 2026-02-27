package SKU;

import java.util.ArrayList;

public class SKUList {
    private final ArrayList<SKU> skuList;

    public SKUList() {
        this.skuList = new ArrayList<SKU>();
    }

    public int getSize() {
        return this.skuList.size();
    }

    public boolean isEmpty() {
        return skuList.isEmpty();
    }

    public void addSKU(String skuID, Location skuLocation) {
        SKU sku = new SKU(skuID, skuLocation);
        skuList.add(sku);
    }

    public void deleteSKU(String skuID) {
        skuList.removeIf(sku -> sku.getSKUID().equals(skuID));
    }
}
