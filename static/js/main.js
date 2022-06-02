function validateAge() {
  var age = document.getElementById("age").value;
  if (!age.match(/^\b([0-9]|[1-9][0-9]|100)\b/)) {
    document.getElementById("age").value = "";
    document.getElementById("age").placeholder = "Enter valid age";
  }
  if (age < 18) {
    document.getElementById("age").value = "";
    document.getElementById("age").placeholder =
      "Sorry, You age is " + age + " and you are not eligible for test";
  }
}
