pragma solidity ^0.4.25;
contract Supply{
    struct Company{
        string name;
        address addr;
        bool isExisted;
    }

    //from 欠 to 
    struct Receipt{
        address borrower;
        address lender;
        uint money;
        string info;
        uint date;
        bool isFinaced;//是否已经拿去做银行融资
        bool confirmed;
    }

    struct Index{
        uint Index;
        uint Index1;
        uint Index2;
    }
    address public bankAdd;    
    mapping(address => Company) public addr2Company;
    mapping(address => Receipt[]) public comp2Receipt;

    constructor() public{
        bankAdd = msg.sender;   
     //   addr2Company[bankAdd] = Company("bank", bankAdd, 0, true);
    }

    function getReceiptLength(address comp) public returns(uint){
        return comp2Receipt[comp].length;
    }
   
    function getReceipt(address comp, uint index) public returns( address borrower,
        address lender,
        uint money,
        string info,
        uint date,
        bool isFinaced,//是否已经拿去做银行融资
        bool confirmed){
        Receipt rec = comp2Receipt[comp][index];
        return (rec.borrower,
                rec.lender,
                rec.money,
                rec.info,
                rec.date,
            rec.isFinaced,rec.confirmed);

    }

     //function1: buy from comp and make a check
    function buyAndCheck(address lender, uint money, string memory info) public returns(string){
        //判断是否有这几家公司
        address borrower = msg.sender;
//        if(!addr2Company[borrower].isExisted)
        addr2Company[borrower] = Company("", borrower, true);
  //      if(!addr2Company[lender].isExisted)
        addr2Company[lender] = Company("",lender, true);

        //from和to都要记录 
        uint date1 = now;
        comp2Receipt[borrower].push(Receipt(borrower, lender, money, info, date1,false,false));
        comp2Receipt[lender].push(Receipt(borrower, lender, money, info, date1,false,false));
        
        return info;
    }

    //function2: transfer check
    function transferCheck(address borrower, address newLender, uint money, string memory info) public{
        //borrower和oldLender之间的欠条金额减去money：找到对应的欠条
        uint index =  0;
        for(index = 0; index < comp2Receipt[borrower].length; index++){
            if(comp2Receipt[borrower][index].borrower == borrower && comp2Receipt[borrower][index].lender == msg.sender && comp2Receipt[borrower][index].money >= money){
                comp2Receipt[borrower][index].money -= money;
                break;
            }
        }
        for(index = 0; index < comp2Receipt[msg.sender].length; index++){
            if(comp2Receipt[msg.sender][index].borrower == borrower && comp2Receipt[msg.sender][index].lender == msg.sender && comp2Receipt[msg.sender][index].money >= money){
                comp2Receipt[msg.sender][index].money -= money;
                break;
            }
        }
        //oldLender和newLender之间的欠条减去money：找到对应的欠条
        for(index = 0; index < comp2Receipt[msg.sender].length; index++){
            if(comp2Receipt[msg.sender][index].borrower == msg.sender && comp2Receipt[msg.sender][index].lender == newLender && comp2Receipt[msg.sender][index].money >= money){
                comp2Receipt[msg.sender][index].money -= money;
                break;
            }
        }
        for(index = 0; index < comp2Receipt[newLender].length; index++){
            if(comp2Receipt[newLender][index].borrower == msg.sender && comp2Receipt[newLender][index].lender == newLender && comp2Receipt[newLender][index].money >= money){
                comp2Receipt[msg.sender][index].money -= money;
                break;
            }
        }
        //borrower和newLender之间的欠条金额加上money：直接新增一个欠条 info
        uint date = now;
        comp2Receipt[newLender].push(Receipt(borrower, newLender, money, info, date, false, false));
        comp2Receipt[borrower].push(Receipt(borrower, newLender, money, info, date, false, false));
    }


    //function3: borrow money from bank
    function borrowMoney(uint money, uint receipt_idx)public{
        if(comp2Receipt[msg.sender][receipt_idx].isFinaced)
            revert("The receipt have been used to finace.");
        if(comp2Receipt[msg.sender][receipt_idx].money < money)
            revert("The amount of money to be borrowed is greater than the limit");
        comp2Receipt[msg.sender][receipt_idx].isFinaced = true;
    }

    

    //function4: settle check
    function settleCheck(uint receipt_idx)public{
        Receipt storage rec = comp2Receipt[msg.sender][receipt_idx];
        uint index;
        bool flag = false;//判断是否settle
        for(index = 0; index < comp2Receipt[msg.sender].length; index++){
            if(comp2Receipt[msg.sender][index].borrower == rec.borrower && comp2Receipt[msg.sender][index].lender == rec.lender){
                if(comp2Receipt[msg.sender][index].money == rec.money){
                    uint index2;
                    address to = rec.lender;
                    uint date4 = now;
                    for(index2 = 0; index2 < comp2Receipt[to].length; index2++){
                        if(comp2Receipt[to][index2].borrower == rec.borrower && comp2Receipt[to][index2].lender == rec.lender){
                            if(comp2Receipt[to][index2].money == rec.money){
                                delete comp2Receipt[to][index2];
                                comp2Receipt[to][index2].date = date4;
                                comp2Receipt[to][index2].info = "settled";
                                break;
                            }
                        }
                    }
                    delete comp2Receipt[msg.sender][index];
                    comp2Receipt[msg.sender][index].date = date4;
                    comp2Receipt[msg.sender][index].info = "settled";
                    flag = true;
                    break;
                }
            }
        }
        if(!flag)
            revert("fake receipt!");
    }

    
    //confirm a receipt
    function confirm(address comp,uint receipt_idx)public{
        if(msg.sender != bankAdd)
            revert("permission denied: not bank account");
        comp2Receipt[comp][receipt_idx].confirmed = true;
    }

}

