package iterator;

public class BCafeMenu implements Menu {
	static final int MAX_ITEMS = 6;
	int numberOfItems = 0;
	MenuItem[] menuItems;
  
	public BCafeMenu() {
		menuItems = new MenuItem[MAX_ITEMS];
 
		addItem("야미버거", "흠냐흠냐", true, 2.99);
		addItem("배리굿버거", "마시써!", false, 1.5);

	}
  
	public void addItem(String name, String description, boolean vegetarian, double price) {
		MenuItem menuItem = new MenuItem(name, description, vegetarian, price);
		if (numberOfItems < MAX_ITEMS) {
			menuItems[numberOfItems] = menuItem;
			numberOfItems = numberOfItems + 1;
		}
	}
 
	public MenuItem[] getMenuItems() {
		return menuItems;
	}
  
	public Iterator createIterator() {
		return new BCafeMenuIterator(menuItems);
	}
}
