package composite.menu;

public class Main {
	public static void main(String args[]) {
		MenuComponent aCafeMenu = new Menu("ACafeMenu", "Breakfast");
		MenuComponent bCafeMenu = new Menu("BCafeMenu", "Lunch");

		MenuComponent allMenus = new Menu("ALL MENUS", "모든 메뉴");
  
		allMenus.add(aCafeMenu);
		allMenus.add(bCafeMenu);

		aCafeMenu.add(new MenuItem("기름진 아침A", "냠냠", false, 1));
		aCafeMenu.add(new MenuItem("채식 아침B", "쩝쩝", true, 2));

		bCafeMenu.add(new MenuItem("야미버거", "흠냐흠냐", true, 2.99));
		bCafeMenu.add(new MenuItem("배리굿버거", "마시써!", false, 1.5));


		Waitress waitress = new Waitress(allMenus);
   
		waitress.printMenu();
	}
}
