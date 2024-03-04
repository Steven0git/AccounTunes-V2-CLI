-- Table: info
-- This table stores general information related to transactions.
CREATE TABLE info (
    id INTEGER PRIMARY KEY,  
    name TEXT,  
    type TEXT CHECK(type IN ('income', 'expenditure', 'planned_exp', 'record')),  
    description TEXT,  
    trans_id INTEGER,  
    FOREIGN KEY(trans_id) REFERENCES `transaction`(id)  
);

-- Table: `transaction`
-- This table stores actual transactions, categorized as income or expenditure.
CREATE TABLE `transaction` (
    id INTEGER PRIMARY KEY,  
    type TEXT CHECK(type IN ('income', 'expenditure')),
    amount REAL,  
    date DATE  
);

-- Table: transaction_plan
-- This table is used to track planned expenditures.
CREATE TABLE transaction_plan (
    id INTEGER PRIMARY KEY,  
    amount REAL NOT NULL,  
    date_start DATE NOT NULL,  
    date_end DATE NOT NULL,  
    trans_id INTEGER NOT NULL,  
    FOREIGN KEY(trans_id) REFERENCES info(id)  
);

-- Table: eval_transaction
-- This table records evaluations of transactions on a weekly basis.
CREATE TABLE eval_transaction (
    id INTEGER PRIMARY KEY,  
    total REAL NOT NULL,  
    saved REAL NOT NULL,  
    date DATE NOT NULL,  
    info_id INTEGER,  
    FOREIGN KEY(info_id) REFERENCES info(id)  
);

-- Table: log_trans
-- This table logs increments or decrements in transaction amounts.
CREATE TABLE log_trans (
    id INTEGER PRIMARY KEY,  
    date DATETIME,  
    type TEXT CHECK(type IN ('income', 'expenditure')),  
    trans_id INTEGER,  
    FOREIGN KEY(trans_id) REFERENCES `transaction`(id)  
);

-- Trigger: log_transaction_trigger
-- This trigger logs transactions after they are inserted into the transaction table.
CREATE TRIGGER log_transaction_trigger AFTER INSERT ON `transaction`
BEGIN
    INSERT INTO log_trans (date, type, trans_id)  
    VALUES (NEW.date, NEW.type, NEW.id);
END;