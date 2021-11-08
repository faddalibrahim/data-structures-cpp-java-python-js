class Node {
  constructor(data, next = null) {
    this.data = data;
    this.next = next;
  }
}

class SinglyLinkedList {
  head = null;
    tail = null;
    
    static isEmpty()

  addLast(data) {
    let newNode = new Node(data);

    if (this.head == null) {
      this.head = this.tail = newNode;
      //   this.head = this.tail = new Node(data);
    } else {
      this.tail.next = newNode;
      this.tail = newNode;
      // this.tail.next = this.tail = new Node(data)
    }
  }

  printData() {
    let currentNode = this.head;
    while (currentNode !== null) {
      console.log(currentNode.data);
      currentNode = currentNode.next;
    }
  }
}

const sll = new SinglyLinkedList();
sll.addLast(12);
sll.addLast(13);
sll.addLast(15);
sll.addLast(16);

console.log(sll);
sll.printData();

// console.log(SinglyLinkedList.isEmpty());
