package iterator;

import java.util.ArrayList;
import java.util.List;

public class ACafeMenu implements Menu {
	List<MenuItem> menuItems;
 
	public ACafeMenu() {
		menuItems = new ArrayList<MenuItem>();
    
		addItem("기름진 아침A", "냠냠", false, 1);
		addItem("채식 아침B", "쩝쩝", true, 2);

	}

	public void addItem(String name, String description, boolean vegetarian, double price) {
		MenuItem menuItem = new MenuItem(name, description, vegetarian, price);
		menuItems.add(menuItem);
	}
 
	public List<MenuItem> getMenuItems() {
		return menuItems;
	}
  
	public Iterator createIterator() {
		return new ACafeMenuIterator(menuItems);
	}

}
