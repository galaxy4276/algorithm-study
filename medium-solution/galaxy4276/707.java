/**
 * MyLinkedList() Initializes the MyLinkedList object.
 * int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
 * void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
 * void addAtTail(int val) Append a node of value val as the last element of the linked list.
 * void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
 * void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 *
 */
class MyLinkedList {

  private final Node head = new Node(0), tail = new Node(0);
  private int length = 0;

  public MyLinkedList() { head.next = tail; }


  static class Node {

    public int val;
    public Node next;

    public Node() {}

    public Node(int val) {
      this.val = val;
    }

    public Node(int val, Node next) {
      this.val = val;
      this.next = next;
    }

  }

  public int get(int i) {
    if (i >= length) return -1;
    Node node = findPrev(i);
    return node.next.val;
  }

  public void addAtHead(int val) { addAtIndex(0, val);}

  public void addAtTail(int val) { addAtIndex(length, val);}

  public void addAtIndex(int i, int val) {
    if (i > length) return;
    Node prev = findPrev(i), next = prev.next;
    prev.next = new Node(val);
    prev.next.next = next;
    length++;
  }

  public void deleteAtIndex(int i) {
    if (i >= length) return;
    Node prev = findPrev(i);
    prev.next = prev.next.next;
    length--;
  }


  Node findPrev(int i) {
    Node node = head;
    while (i-- > 0) node = node.next;
    return node;
  }

  public Node getTail() {
    return this.tail;
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    Node node = head.next;
    while (node != null) {
      if (sb.toString().equals("")) {
        sb.append(node.val);
        node = node.next;
      } else {
        sb.append("->").append(node.val);
        node = node.next;
      }
    }

    return sb.toString();
  }

}

public class Main {

  public static void main(String[] args) {
    MyLinkedList linkedList = new MyLinkedList();
    linkedList.addAtHead(1);
    System.out.println(linkedList.toString());
    linkedList.addAtTail(3);
    System.out.println(linkedList.toString());
    linkedList.addAtIndex(1, 2);
    System.out.println(linkedList.toString());
    System.out.println(linkedList.get(1));
    linkedList.deleteAtIndex(1);
    System.out.println(linkedList.toString());
  }
}
