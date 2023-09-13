DELIMITER $$
CREATE TRIGGER RULEFOUR `payment` AFTER INSERT ON `payment` FOR EACH ROW
BEGIN
	INSERT INTO records SET receipts = NEW.amt;
END$$

CREATE TRIGGER RULEEIGHT  `service` BEFORE INSERT ON `service` FOR EACH ROW
BEGIN
	IF NEW.custID IN (SELECT custID FROM account WHERE type = "employers")
		THEN SET type = EXPEDIATE;
	END IF;
END ;$$

CREATE TRIGGER RULENINE `appointment` AFTER INSERT ON `appointment` FOR EACH ROW
BEGIN
	INSERT INTO service SET custID = NEW.custID;
    INSERT INTO service SET type = "Appointment";
END$$

REATE TRIGGER Ordersupply AFTER UPDATE ON supplies FOR EACH ROW
BEGIN
IF NEW.masks <= 50 THEN
INSERT INTO orders(descriptionO, locID) VALUES ('mask', new.locID);
END IF;
IF NEW.gloves <= 50 THEN
INSERT INTO orders(descriptionO, locID) VALUES ('gloves', new.locID);
END IF;
IF NEW.syringes <= 50 THEN
INSERT INTO orders(descriptionO, locID) VALUES ('syringes', new.locID);
END IF;
END;


DELIMITER ;
