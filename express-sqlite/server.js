const express=require('express');
const sqlite3=require("sqlite3").verbose();
const app=express();
const PORT=5000;

async function DBconnection(){
  try{
    const db= await new sqlite3.Database("./database.sqlite");
  }catch(err){
    console.error(err);
  }
 }
DBconnection();

app.get('/',(req,res)=>{
  res.send({message:"Got connection"})
})
// Middleware to parse JSON bodies
app.use(express.json());

// Sample route to get all users
app.get('/users', (req, res) => {
    db.all('SELECT * FROM users', [], (err, rows) => {
        if (err) {
            res.status(400).json({ error: err.message });
            return;
        }
        res.json({ data: rows });
    });
});
// Sample route to create a new user
app.post('/users', (req, res) => {
  const { name, email } = req.body;
  db.run('INSERT INTO users (name, email) VALUES (?, ?)', [name, email], function(err) {
      if (err) {
          res.status(400).json({ error: err.message });
          return;
      }
      res.json({ id: this.lastID });
  });
});
app.listen(PORT,()=>{
  console.log(`Server is started listening on http://localhost:${PORT}`);
})


process.on('SIGINT',()=>{
	db.close((err)=>{
		if(err){
			console.error('Error in closing database',err.message)
		}else{
			console.log('Database connection closed');
		}
		process.exit(0);
	});
});

