package stack.java;

import java.util.Stack;

public class StringReverser {
    public String reverse(String string) {
        if (string == null) {
            throw new IllegalArgumentException();
        }

        Stack<Character> stack = new Stack<Character>();

        for (char ch : string.toCharArray()) {
            stack.push(ch);
        }

        // String reversed = "";
        // while (!stack.empty()) {
        //     reversed += stack.pop();
        // }

        StringBuffer reversed = new StringBuffer();
        while (!stack.empty()) {
            reversed.append(stack.pop());
        }
        
        return reversed.toString();
    }
}
