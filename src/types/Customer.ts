export interface IReceivedCustomer {
    customerId: string;
    customerFirstName: string;
    customerMiddleName?: string;
    customerLastName: string;
    customerUsername: string;
    customerEmail: string;
    customerContactNumber: string;
    customerIsActive: boolean;
}

export interface ICustomer {
    customerFirstName: string;
    customerMiddleName?: string;
    customerLastName: string;
    customerUsername: string;
    customerPassword: string;
    customerEmail: string;
    customerContactNumber: string;
    customerIsActive: boolean;
}