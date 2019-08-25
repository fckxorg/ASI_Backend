pragma solidity >=0.4.22 <0.6.0;
 
contract Project is Owned {
    string name;
    string description;
    string url;
    uint date = now;
   
}
 
contract Owned {
    address owner;
    event AccessDenied(address account);
 
    modifier onlyOwner() {
        if (msg.sender == owner) {
            _;
        }
        else {
            AccessDenied(msg.sender);
        }
    }
 
    function Owned() {
        owner = msg.sender;
    }
 
    function changeOwner(address _newOwner) onlyOwner {
        owner = _newOwner;
    }
}
