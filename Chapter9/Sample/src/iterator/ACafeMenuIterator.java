package iterator;

import java.util.List;

public class ACafeMenuIterator implements Iterator {
	List<MenuItem> items;
	int position = 0;
 
	public ACafeMenuIterator(List<MenuItem> items) {
		this.items = items;
	}
 
	public MenuItem next() {
		return items.get(position++);
	}
 
	public boolean hasNext() {
		return items.size() > position;
	}
}
