var result = ""
var memory = 0

const buttons = document.querySelectorAll('.btn')

Array.from(buttons).forEach((button) => {
    
    button.addEventListener("click", (e)=>{
        console.log(e.target.closest("div").dataset)

        // result
        if(e.target.innerHTML == "="){
            result = eval(result)
            document.querySelector('input').value = result;

        } 
        // clear display
        else if(e.target.innerHTML == "C"){
            result = "" 
            document.querySelector('input').value = result

        } 
        // clear memory 
        else if(e.target.innerHTML == "MC"){
            memory = 0;

        } 
        // save memory
        else if(e.target.innerHTML == "MS"){
            memory = result;

        } 
        // square 
        else if(e.target.innerText == 'x2'){
            result = result ** 2;
            document.querySelector('input').value = result;
        }        
        // backspace
        else if (e.target.closest("div").dataset.type == "bs"){
            result = result.slice(0,-1)
            document.querySelector('input').value = result;
        }
        // absolute
        else if (e.target.innerHTML == "|x|"){
            result = Math.abs(Number(result))
            document.querySelector('input').value = result;
        }

        // 1/x
        else if (e.target.innerHTML == "1/x"){
            result = 1/Number(result)
            document.querySelector('input').value = result;

        }
        // exp
        else if (e.target.innerHTML == "exp"){
            result = result + "**" 
            // console.log("exp pressed")
        }
        //mod 
        else if (e.target.innerHTML == "mod"){
            result = Number(result) + "%"
            // document.querySelector('input').value = result;

            //issue -- 10%3 display pr dikh rha h

        }
        // square root
        else if(e.target.innerHTML == 'x2R'){
            result = Math.sqrt(Number(result))
            document.querySelector('input').value = result;
        }   
        // factorial
        else if(e.target.innerHTML == 'n!') {
            num = Number(result)
            function factorialize(num) {
                if (num < 0) 
                      return -1;
                else if (num == 0) 
                    return 1;
                else {
                    return (num * factorialize(num - 1));
                }
              }            
            result = factorialize(num)
            document.querySelector('input').value = result;    
        }
        // log
        else if(e.target.innerHTML == 'log'){
            result = Math.log(Number(result))
            document.querySelector('input').value = result;
        }
        // 10**x
        else if(e.target.innerHTML == '10P'){
            num = Number(result)
            result = Math.pow(10,num)
            // result = Math.log(Number(result))
            document.querySelector('input').value = result;
        }







        else {
        // console.log(e.target)
        result = result + e.target.innerHTML;
        document.querySelector('input').value = result;



        // if(result == ""){
        //     document.querySelector('input').value = result;
        // }
        // else{
        //     document.querySelector('input').value = " ";

        // }
        }
    }) 
})