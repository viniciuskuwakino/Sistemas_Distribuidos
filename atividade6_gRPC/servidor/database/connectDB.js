/**
 * Configuracao do Knex, passando o parametro "client" que determina qual banco de dados será utlizado,
 * e em seguida 
 */

import knex from "knex"

const connectionDB = knex({
  client: 'sqlite3', // or 'better-sqlite3'
  connection: {
    filename: "./database/database_com_dados-contrib-Daniel-Farina.db"
  },
  useNullAsDefault: true
})

export default connectionDB;