// SPDX-License-Identifier: MIT

pragma solidity >=0.7.0 <0.9.0;

contract SimpleStorage {
    //public makes the attr to be accessed outside the contract
    uint256 public favoriteNumber;

    struct People {
        uint256 favoriteNumber;
        string name;
    }

    People public person1 = People({favoriteNumber: 10, name: "Simone"});

    People[] public people;
    mapping(string => uint256) public nameToFavouriteNumber;

    function store(uint256 _num) public {
        favoriteNumber = _num;
    }

    function retrieve() public view returns (uint256) {
        return favoriteNumber;
    }

    function addPerson(string memory _name, uint256 _favNum) public {
        people.push(People(_favNum, _name));
        nameToFavouriteNumber[_name] = _favNum;
    }
}
