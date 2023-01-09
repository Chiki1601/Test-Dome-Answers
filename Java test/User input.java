public class UserInput {
    
    public static class TextInput {
        protected StringBuilder inputSB;
        
        public TextInput() {
            inputSB = new StringBuilder();
        }
        
        public void add(char c) {
            this.inputSB.append(c);
        }
        
        public String getValue() {
            return this.inputSB.toString();   
        }
    }

    public static class NumericInput extends TextInput {
        
        public NumericInput() {
            super();
        }
        
        @Override
        public void add(char c) {
            if (Character.isDigit(c)) {
                this.inputSB.append(c);
            }
        }
    }

    public static void main(String[] args) {
        TextInput input = new NumericInput();
        input.add('1');
        input.add('a');
        input.add('0');
        System.out.println(input.getValue());
    }
}
