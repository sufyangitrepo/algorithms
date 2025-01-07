
class HashMap {
    constructor () {
        // table for storing the data
        this.table = new Array(128);
        // what size of table has occupied
        this.size = 0
    }

    _hash(key) {
        let hash = 0
        for(let i = 0; i < key.length; i++){
            const charCode = key.charCodeAt(i)
            hash += charCode
        }
        return hash % key.length;
    }
    
    set(key, value) {
        const hash = this._hash(key)
        if (this.table[hash]) {
            return false
        }
        this.table[hash] = [key, value]
        this.size++;
        return true
    }

    set_handle_collision(key, value) {
        const hash = this._hash(key)
        if (this.table[hash] && this.table[hash].length) {
            for (let i=0; i > this.table[hash].length; i++){
                if (this.table[hash][i][0] == key){
                    this.table[hash][i][1] = value
                    return false
                }
            }
            this.table[hash].push([key, value])
            this.size++;
            return
        }
        this.table[hash] = []
        this.table[hash].push([key, value])
        this.size++;
        return true
    }


    get(key) {
        const hash = this._hash(key)
        if (this.table[hash] && this.table[hash].length){
            for (let i = 0; i < table[hash].length; i++ ){
                if (table[hash][i][0] === key){
                    return this.table[hash][i];
                }
            }
        }
        return null;
    }

    remove(key) {
        const hash = this._hash(key)
        if (this.table[hash] && this.table[hash].length) {
            for (let i = 0; i < table[hash].length; i++ ){
                if (table[hash][i][0] === key){
                    this.table[hash].splice(i, 1);
                    this.size--;
                    return true
                }
            }
        }
        return false;
    }

    show() {
        this.table.forEach((item, ind) => {
            if (item.length) {
                item.forEach((data) => {
                    console.log(`{ ${data[0]}: ${data[1]}}`);
                })
            }
        
        })
    }
}


const hash = new HashMap();
hash.set_handle_collision("Spain", 110);
hash.set_handle_collision("ǻ", 192);
console.log(hash.show());




