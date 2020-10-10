pragma solidity ^0.6.0;

contract Balance {

    
    //this returns th balance on the contract
    function getBalance() public view returns(uint) {
        return address(this).balance;
    }
    
    //this allows you to send ETH to the contract
    function sendMoney() public payable {

    }
    
    //this function withdraws all money stored in the smart contract
    //but only to the initial address that sent money.
    
    function withdrawAllMoney(address payable _to) public {
        _to.transfer(address(this).balance);
    }
}
