let optionCount = 2;

function addOption() {
    let newOption = document.createElement("div");
    newOption.className = "input-group m-10";
    optionCount++;
    newOption.id = "option" + optionCount; 
    document.getElementById("options").appendChild(newOption);
    newOption.innerHTML = `<input name="option${optionCount}" type="text" class="form-control" id="option${optionCount}" placeholder="Option ${optionCount}" value="Option ${optionCount}" required="required" />
                            <button onclick="removeOption(${optionCount})" class="btn btn-square ml-10" type="button">&times;</button>
                            `;
}

function removeOption(id) {
    document.getElementById(`option${id}`).remove();
    optionCount--;
}
