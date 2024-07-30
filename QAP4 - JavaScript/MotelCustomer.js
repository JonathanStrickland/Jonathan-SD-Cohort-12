// Description: QAP 4 - JavaScript
// Name: Jonathan Strickland
// Date: July 22th 2024

// Identifying Customer Information
class Customer {
    constructor(Name, BirthDate, Gender, RoomPref, PayMethod, MailAddress, PhoNum, CheckIn, CheckOut) {
        this.Name = Name;
        this.BirthDate = new Date(BirthDate);
        this.Gender = Gender;
        this.RoomPref = RoomPref;
        this.PayMethod = PayMethod;
        this.MailAddress = MailAddress;
        this.PhoNum = PhoNum;
        this.CheckIn = new Date(CheckIn);
        this.CheckOut = new Date(CheckOut);
    }

    // Calculate the Age
    Age() {
        const Today = new Date();
        let Age = Today.getFullYear() - this.BirthDate.getFullYear();
        const MonthDifference = Today.getMonth() - this.BirthDate.getMonth();
        if (MonthDifference < 0 || (MonthDifference === 0 && Today.getDate() < this.BirthDate.getDate())) {
            Age--;
        }
        return Age;
    }

    // Calculate the Stay Duration
    StayDuration() {
        const duration = this.CheckOut - this.CheckIn;
        return Math.ceil(duration / (1000 * 60 * 60 * 24));
    }

    // Customer Description
    CustomerDescription() {
        return `
            Name: ${this.Name}
            Age: ${this.Age()}
            Gender: ${this.Gender}
            Room Preferences: ${this.RoomPref.join(', ')}
            Payment Method: ${this.PayMethod}
            Mailing Address: ${this.MailAddress.Street}, ${this.MailAddress.City}, ${this.MailAddress.Province} ${this.MailAddress.PostalCode}
            Phone Number: ${this.PhoNum}
            Check-In Date: ${this.CheckIn.toDateString()}
            Check-Out Date: ${this.CheckOut.toDateString()}
            Duration of Stay: ${this.StayDuration()} day(s)

            The customers name is ${this.Name}, they are ${this.Age()} and the customer is ${this.Gender}. ${this.Name} room preference was ${this.RoomPref.join(', ')} 
            and will be staying with us from ${this.CheckIn.toDateString()} to ${this.CheckOut.toDateString()},which is a total of ${this.StayDuration()} days. 
            Some confidental information about ${this.Name} is their mailing address which is ${this.MailAddress.Street}, ${this.MailAddress.City}, ${this.MailAddress.Province} ${this.MailAddress.PostalCode} and their phone number which is ${this.PhoNum}.
        `;
    }
}

// Example for Outputs
const customer = new Customer(
    'John Doe',
    '1985-06-15',
    'Male',
    ['King Bed', 'Non-Smoking'],
    'Credit Card',
    {
        Street: '123 Main St',
        City: 'St. Johns',
        Province: 'NL',
        PostalCode: 'A1B 2C3'
    },
    '555-1234',
    '2024-07-01',
    '2024-07-10'
);

// Console Output
console.log(customer.CustomerDescription());

// HTML Output
document.addEventListener('DOMContentLoaded', () => {
    const customerInfoDiv = document.getElementById('customerInfo');
    customerInfoDiv.innerHTML = `<pre>${customer.CustomerDescription()}</pre>`;
});