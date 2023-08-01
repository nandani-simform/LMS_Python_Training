let result = "";
let answer = 0;
let memory = 0;
let flag = false;
let hasMemory = 0;
let lastEnteredNumber = 0;

const buttons = document.querySelectorAll(".btn");

Array.from(buttons).forEach((button) => {
  button.addEventListener("click", (e) => {

    // result
    if (e.target.innerHTML == "=") {
      if (flag) {
        result = answer + lastEnteredNumber;
        flag = false;
      }
      result = eval(result);
      lastEnteredNumber = result;
      document.querySelector("input").value = result;
    }
    // clear display
    else if (e.target.innerHTML == "C") {
      result = "";
      document.querySelector("input").value = result;
    }
    // clear memory
    else if (e.target.innerHTML == "MC") {
      memory = 0;
      // document.querySelector('input').value = 0
    }
    // result memory
    else if (e.target.innerHTML == "MR") {
      console.log(memory, "memory result");
      result = memory;
      document.querySelector("input").value = result;
    }
    // save memory
    else if (e.target.innerHTML == "MS") {
      console.log(memory, "memory save");
      result = memory;
      // document.querySelector("input").value = result;
    }
    // memory +
    else if (e.target.innerHTML == "M+") {
      hasMemory = true;
      memory = Number(memory) + Number(lastEnteredNumber);
      //   console.log(memory, "M+");
      document.querySelector("input").value = lastEnteredNumber;
    }
    // memory -
    else if (e.target.innerHTML == "M-") {
      hasMemory = true;
      memory = Number(memory) - Number(lastEnteredNumber);
      document.querySelector("input").value = lastEnteredNumber;
    }
    // square
    else if (e.target.innerText == "x2") {
      result = result ** 2;
      document.querySelector("input").value = result;
    }
    // backspace
    else if (e.target.closest("div").dataset.type == "bs") {
      result = result.slice(0, -1);
      document.querySelector("input").value = result;
    }
    // absolute
    else if (e.target.innerHTML == "|x|") {
      result = Math.abs(Number(result));
      document.querySelector("input").value = result;
    }
    // 1/x
    else if (e.target.innerHTML == "1/x") {
      result = 1 / Number(result);
      document.querySelector("input").value = result;
    }
    // exp
    else if (e.target.innerHTML == "exp") {
      result = result + "**";
      // console.log("exp pressed")
    }
    // square root
    else if (e.target.closest("div").dataset.type == "root") {
      result = Math.sqrt(Number(result));
      document.querySelector("input").value = result;
    }
    // factorial
    else if (e.target.innerHTML == "n!") {
      num = Number(result);
      function factorialize(num) {
        if (num < 0) return -1;
        else if (num == 0) return 1;
        else {
          return num * factorialize(num - 1);
        }
      }
      result = factorialize(num);
      document.querySelector("input").value = result;
    }
    // log
    else if (e.target.innerHTML == "log") {
      result = Math.log(Number(result));
      document.querySelector("input").value = result;
    }
    // 10**x
    else if (e.target.closest("div").dataset.type == "10P") {
      num = Number(result);
      result = Math.pow(10, num);
      document.querySelector("input").value = result;
    }
    // x-raisedTo-y
    else if (e.target.closest("div").dataset.type == "x-raised-to-y") {
      answer = Number(result) + "**";
      result = Number(result) + "^";
      flag = true;
      document.querySelector("input").value = result;
    }
    //mod
    else if (e.target.innerHTML == "mod") {
      answer = Number(result) + "%";
      result = Number(result) + "%";
      flag = true;
      document.querySelector("input").value = result;
    }
    // pi
    else if (e.target.closest("div").dataset.type == "pi") {
      result = Number(result) * 3.14;
      document.querySelector("input").value = result;
    }
    // percent %
    else if (e.target.innerHTML == "%") {
      result = Number(result) / 100;
      document.querySelector("input").value = result;
    } 
    // sin
    else if (e.target.closest('div').dataset.type == "disabled") {
      document.querySelector("input").value = 0;
    }
    else {
      lastEnteredNumber = e.target.innerHTML;
      if (hasMemory && e.target.closest("div").dataset.type == "number") {
        result = lastEnteredNumber;
      } else {
        result = result + lastEnteredNumber;
      }
      hasMemory = false;
      document.querySelector("input").value = result;
    }
  });
});
