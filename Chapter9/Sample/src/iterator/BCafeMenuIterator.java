package iterator;

public class BCafeMenuIterator implements Iterator {
	MenuItem[] list;
	int position = 0;

	public BCafeMenuIterator(MenuItem[] list) {
		this.list = list;
	}
	public MenuItem next() {
		return list[position++];
	}
	public boolean hasNext() {
		if (position >= list.length || list[position] == null) {
			return false;
		} else {
			return true;
		}
	}
}
