//SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.0;

contract Bank{
    address private accOwner;
    uint256 balance=0;
    constructor(){
        accOwner=msg.sender;
    }

    function Deposit() public payable{
        require(accOwner==msg.sender,"You are not an account owner!!");
        require(msg.value > 0, "Amount should be greater than 0.");
        balance+=msg.value;
    }

    function Withdraw() public payable {
        require(accOwner==msg.sender,"You are not an account owner");
        require(msg.value > balance,"Account doesnot have sufficient balance!");
        balance-=msg.value;
    }

    function showBalance() public view returns(uint256){
        require(accOwner==msg.sender,"You are not an account owner");
        return balance;
    }
}