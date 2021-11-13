package stack.java;

import java.util.Stack;

public class BalancedExpressions {
    public Boolean isBalanced(String expression) {
        Stack<Character> stack = new Stack<Character>();

        for (char ch : expression.toCharArray()) {
            if (isLeftBracket(ch)) {
                stack.push(ch);
            }

            if (isRightBracket(ch)) {
                if (stack.empty())
                    return false;
                var top = stack.pop();
                if (bracketsMatch(top,ch)) {
                    return false;
                }
            }

            return stack.empty();

        }
        return stack.empty();
    }
    
    private boolean isLeftBracket(char ch) {
        return ch == '(' || ch == '<' || ch == '[' || ch == '{';
    }
    
    private boolean isRightBracket(char ch) {
        return ch == ')' || ch == '>' || ch == ']' || ch == '}';
    }
    
    private boolean bracketsMatch(char left, char right) {
        return (right == ')' && left != '(') || (right == '>' && left != '<') || (right == ']' && left != '[')
                || (right == '}' && left != '{');
    }
}
