function doSomething() {
    let input1 = document.getElementById("inputA").value;
    let input2 = document.getElementById("inputB").value;
    document.getElementById("valueA").innerHTML = input1;
    document.getElementById("valueB").innerHTML = input2;
    document.getElementById("valueC").innerHTML = Number(input1) + Number(input2);
  }

  function whatTimeIsIt() {
      alert(new Date())
  }