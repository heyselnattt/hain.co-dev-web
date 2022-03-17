export interface IReceivedStaff {
    staffId: string;
    staffFullName: string;
    staffContactNumber: string;
    staffUsername: string;
    staffAddress: string;
    staffPosition: CanteenPosition;
    staffIsActive: boolean;
}

export interface IStaff {
    staffFullName: string;
    staffContactNumber: string;
    staffUsername: string;
    staffPassword: string;
    staffAddress: string;
    staffPosition: CanteenPosition;
    staffIsActive: boolean;
}

export enum CanteenPosition {
    CHEF = 1,
    CASHIER,
    SERVER
}