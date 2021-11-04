var maximumWealth = function(accounts) {
    
    wealth = 0;
    
    for(let row=0; row<accounts.length; row++){
        rowSum = 0;
        
        for(let col = 0; col < accounts[row].length; col++){
            rowSum += accounts[row][col] 
        }
        
        if(wealth < rowSum){
            wealth = rowSum
        }
   }
   return wealth;
};
