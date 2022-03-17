export interface IReceivedAdmin {
    adminId: string;
    adminFullName: string;
    adminUsername: string;
    adminPosition: number;
    adminIsActive: boolean;
}

export interface IAdmin {
    adminFullName: string;
    adminUsername: string;
    adminPassword: string;
    adminPosition: AdminPosition;
    adminIsActive: boolean;
}

export enum AdminPosition {
    SUPER_ADMIN = 1,
    SUB_ADMIN
}