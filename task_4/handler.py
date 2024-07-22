from typing import List
from contacts import contacts
from decorators import input_error


@input_error
def add_contact(args: List) -> str:
    if len(args) < 2:
        raise ValueError("Enter username and phone number")

    name, phone = args
    if name in contacts:
        raise ValueError("User already exists")

    contacts[name] = phone
    message = "Contact added"
    return message


@input_error
def change_contact(args: List) -> str:
    if len(args) < 2:
        raise ValueError("Enter username and phone number")

    name, phone = args
    if name not in contacts:
        raise ValueError("User does not exist")

    contacts[name] = phone
    message = "Contact changed"
    return message


@input_error
def show_phone(args: List) -> str:
    if len(args) < 1:
        raise ValueError("Enter username")
    if args[0] not in contacts:
        raise ValueError("User does not exist")
    return contacts.get(args[0])


@input_error
def show_all(args: List) -> str:
    if len(args) > 0:
        raise ValueError("Invalid command")
    return str(contacts)
