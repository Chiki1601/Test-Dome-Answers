<?php
//answer for https://www.testdome.com/questions/php/user-input/15404?visibility=17&skillId=5
class TextInput
{
    public $String= '';
    public function add($input)
    {
        $this->String=$this->String.$input;
        return $this->String;
    }
    public function getValue()
    {
        return $this->String;
        
    }
}

class NumericInput extends TextInput
{
    function add($input)
    {

        if( preg_match('/^\d+$/',$input)){
        $this->String=$this->String.$input;    
        }
        

    }
}

$input = new NumericInput();
$input->add('1');
$input->add('a');
$input->add('0');
echo $input->getValue();
