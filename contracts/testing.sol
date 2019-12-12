pragma solidity ^0.4.25;

contract Supply{
    struct Company{
        string name;
        address addr;
        uint balance;
        bool isExisted;
    }
    
    //from 欠 to 
    struct Receipt{
        address from;
        address to;
        uint money;
        bool confirmed;
        string info;
    }
    
    address public bankAdd;
    
    mapping(address => Company) public addr2Company;
    mapping(address => Receipt[]) public comp2Receipt;
    
    constructor() public{
        bankAdd = msg.sender;   
     //   addr2Company[bankAdd] = Company("bank", bankAdd, 0, true);
    }
    
    //function1: buy from comp and make a check
    function buyAndCheck(address comp, uint money, string memory info) public{
        //判断是否有这几家公司
        if(!addr2Company[msg.sender].isExisted)
            addr2Company[msg.sender] = Company("", msg.sender, 0, true);
        if(!addr2Company[comp].isExisted)
            addr2Company[comp] = Company("",comp,0, true);
        
        //from和to都要记录 
        Receipt memory newCheck = Receipt(msg.sender, comp, money, false, info);
        comp2Receipt[msg.sender].push(newCheck);
        comp2Receipt[comp].push(newCheck);
    }
    
    //function2: transfer check
    function transferCheck(address a, address c,uint money, string memory info)public{
        //a借b b借c
        address b = msg.sender;
        
        //判断是否有这几家公司
        if(!addr2Company[a].isExisted || !addr2Company[b].isExisted || !addr2Company[c].isExisted)
            revert('company not exists.');
        
        //找出a和c b和c之间的欠条
        uint index;
        uint index1;
        uint index2;
        bool flag1 = false;
        bool flag2 = false;
      
        for(index = 0; index < comp2Receipt[b].length; index++){
            //a欠b的
            if(!flag1 && comp2Receipt[b][index].from == a && comp2Receipt[b][index].to == b){
                flag1 = true;
                index1 = index;
            }
            //b欠c的
            if(!flag2 && comp2Receipt[b][index].from == b && comp2Receipt[b][index].to == c
                && comp2Receipt[b][index].money >= money){
                flag2 = true;
                index2 = index;
            }
            if(flag1 && flag2) break;
        }
        
        if(!flag1 || !flag2) 
            revert('receipt not exists.');
        
        //欠条转移
        //a欠b变成a欠c
        //情况1：b对c的全部欠款归到a欠c（即变成a欠b，a欠c）
        if(comp2Receipt[b][index1].money > money){
            //因为收据是双方拥有，所以还要修改a存放的收据
            for(index = 0; index < comp2Receipt[a].length; index++){
                if(comp2Receipt[a][index].from == a && comp2Receipt[a][index].to == b 
                    && comp2Receipt[a][index].money == comp2Receipt[b][index1].money){
                    comp2Receipt[a][index].money -= money;
                    break;
                }
            }
             comp2Receipt[b][index1].money -= money;
             //增加a欠c
            Receipt memory newCheck = Receipt(a, c, money, false, info);
            comp2Receipt[a].push(newCheck);
            comp2Receipt[c].push(newCheck);
        }
        
        
        //情况2：b对c的部分欠款归到a欠c（即a欠c,b欠c）
        else{
            //修改a欠b的账单(a欠b的钱变成a欠c)
            for(index = 0; index < comp2Receipt[a].length; index++){
                if(comp2Receipt[a][index].from == a && comp2Receipt[a][index].to == b 
                    && comp2Receipt[a][index].money == comp2Receipt[b][index1].money){
                        break;
                    }
            }
            uint temp = comp2Receipt[b][index1].money;
            delete comp2Receipt[a][index];
            delete comp2Receipt[b][index1];
            Receipt memory newCheck2 = Receipt(a, c, temp, false, info);
            comp2Receipt[a].push(newCheck2);
            comp2Receipt[c].push(newCheck2);
            //修改b欠c的账单
            if(temp < money){//等于的话b就不欠c
                comp2Receipt[b][index2].money -= temp;
                for(index = 0; index < comp2Receipt[c].length; index++){
                    if(comp2Receipt[c][index].from == b && comp2Receipt[c][index].to == c 
                        && comp2Receipt[c][index].money >= money){
                            comp2Receipt[c][index2].money -= temp;
                            break;
                        }
                }
            }
        }
    }
    
    //function3: borrow money from bank
    function borrowMoney(uint money, Receipt memory rec)public{
        if(rec.money < money)
            revert('The amount of money to be borrowed is greater than the limit');
        addr2Company[msg.sender].balance += money;
    }
    
    //function4: settle check
    function settleCheck(Receipt memory rec)public{
        uint index;
        bool flag = false;//判断是否settle
        for(index = 0; index < comp2Receipt[msg.sender].length; index++){
            if(comp2Receipt[msg.sender][index].from == rec.from 
            && comp2Receipt[msg.sender][index].to == rec.to
            && comp2Receipt[msg.sender][index].money == rec.money){
                if(addr2Company[msg.sender].balance >= rec.money){
                    uint index2;
                    address to = rec.to;
                    for(index2 = 0; index2 < comp2Receipt[to].length; index2++){
                        if(comp2Receipt[to][index2].from == rec.from 
                            && comp2Receipt[to][index2].to == rec.to
                            && comp2Receipt[to][index2].money == rec.money){
                                delete comp2Receipt[to][index2];
                                break;
                            }
                    }
                    delete comp2Receipt[msg.sender][index];
                    flag = true;
                    break;
                }
            }
        }
        if(!flag)
            revert('fake receipt!');
    }
    
    //confirm a receipt
    function confirm(Receipt memory cheque)public{
        if(msg.sender != bankAdd)
            revert('permission denied: not bank account');
        cheque.confirmed = true;
    }
    
}

