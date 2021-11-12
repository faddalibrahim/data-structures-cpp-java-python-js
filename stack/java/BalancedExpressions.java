package stack.java;

import java.util.Stack;

public class BalancedExpressions {
    public Boolean isBalanced(String expression) {
        Stack<Character> stack = new Stack<Character>();

        for (char ch : expression.toCharArray()) {
            if (ch == '(') {
                stack.push(ch);
            }

            if (ch == ')') {

            }

        }
        return stack.empty();
    }
}
