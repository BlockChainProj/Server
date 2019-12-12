pragma solidity ^0.5.14;

contract HelloWorld{
    string name;

    constructor() public{
       name = "Hello, World!";
    }

    function get() view public returns(string memory){
        return name;
    }

    function set(string memory n) public{
    	name = n;
    }
}
