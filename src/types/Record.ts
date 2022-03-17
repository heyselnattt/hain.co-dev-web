export interface IReceivedRecord {

}

export interface Record {
    recordInterval: RecordInterval;
}

export enum RecordInterval {
    WEEKLY = 7,
    BI_MONTHLY = 14,
    MONTHLY = 30
}