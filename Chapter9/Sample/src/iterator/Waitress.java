package iterator;

public class Waitress {
	Menu breakfast;
	Menu dinner;
 
	public Waitress(Menu breakfast, Menu dinner) {
		this.breakfast = breakfast;
		this.dinner = dinner;
	}
 
	public void printMenu() {
		Iterator breakfastIterator = breakfast.createIterator();
		Iterator dinerIterator = dinner.createIterator();

		printMenu(breakfastIterator);
		printMenu(dinerIterator);

	}
 
	private void printMenu(Iterator iterator) {
		while (iterator.hasNext()) {
			MenuItem menuItem = iterator.next();
			System.out.print(menuItem.getName() + ", ");
			System.out.print(menuItem.getPrice() + " -- ");
			System.out.println(menuItem.getDescription());
		}
	}
}
