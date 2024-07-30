// Description: Final Sprint - JavaScript
// Name: Jonathan Strickland
// Date: July 30th 2024

// Constants for income tax
const IncomeTaxRate = 0.15

// FETCHs and reads the SprintPeople.json
fetch('./SprintPeople.json')
    .then(response => response.json())
    .then(data => {
        // Create Container for people
        const container = document.createElement('div');
        container.id = 'SprintPeopleContainer'

        // Loops through the people in the json file
        data.forEach(SprintPerson => {

            // Create a new <div> for each person
            const SprintPersonDiv = document.createElement('div')
            SprintPersonDiv.className = 'SprintPerson';

            // Add the person's data to the <div>
            SprintPersonDiv.innerHTML = `
                <h2>${getFullName(SprintPerson)}</h2>
                <p>Age: ${getAge(SprintPerson)}</p>
                <p>Gross Income: ${getSalary(SprintPerson)}</p>
                <p>Net Income: ${getNetIncome(SprintPerson)}</p>
                <p>Gender: ${getGender(SprintPerson)}</p>
            `;

            // Add the person's div to the container
            container.appendChild(SprintPersonDiv);

            // Outputs the person information to the console
            console.log(getFullName(SprintPerson));
            console.log(getAge(SprintPerson));
            console.log(getSalary(SprintPerson));
            console.log(getNetIncome(SprintPerson));
            console.log(getGender(SprintPerson));
        });

        // Outs the persons information to the html file
        document.body.appendChild(container);
    })

    // Catches any errors that occur while fetching the file
    .catch(error => {
        console.error(error);
    })

    // Functions

    // Function to get the persons full name
    function getFullName(SprintPerson) {
        return `${SprintPerson.firstname} ${SprintPerson.lastname}`;
    }

    // Function to get the persons age
    function getAge(SprintPerson) {    
        return `${SprintPerson.firstname} is ${new Date().getFullYear() - 
          new Date(SprintPerson.birthday).getFullYear()} years old.`; 
      }
    
    // Function to get the person gender
    function getGender(SprintPerson){
    return SprintPerson.gender;
    }

    // Function to get the persons Salary
    function getSalary(SprintPerson){
    return `Has a yearly salary before taxes of ${SprintPerson.salary}.`;
    }

    // Funtion to calculate the income tax on the persons salary
    function getIncomeTax(SprintPerson){
    return SprintPerson.salary * IncomeTaxRate;
    }

    // Function to get the persons income after taxes
    function getNetIncome(SprintPerson){
    return `Has a yearly salary after taxes of ${SprintPerson.salary - getIncomeTax(SprintPerson)}.`;
    }

