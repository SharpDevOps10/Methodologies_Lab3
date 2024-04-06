const fastify = require('fastify')({ logger: true })

fastify.get('/', function handler (request, reply) {
  reply.send({ message: 'hello singers' })
})

const singers = [
  { id: 1, name: 'Paul Mccartney' },
  { id: 2, name: 'Thom Yorke' },
  { id: 3, name: 'Elvis Presley' },
];

fastify.get('/singers/:id', (request, reply) => {
  const { id } = request.params;
  const singer = singers.find(s => s.id === parseInt(id));
  if (!singer) reply.status(404).send({ message: 'Singer not found' });
  else reply.send(singer);
});

fastify.get('/singers', (request, reply) => {
  reply.send(singers);
});

fastify.post('/singers', (request, reply) => {
  let singers = [];
  const { name } = request.body;
  const newSinger = { id: singers.length + 1, name };
  singers.push(newSinger);
  reply.code(201).send(newSinger);
});

fastify.listen(8080, '0.0.0.0', (err, address) => {
  if (err) {
    fastify.log.error(err)
    process.exit(1)
  }
  console.log(`Server listening at ${address}`);
});