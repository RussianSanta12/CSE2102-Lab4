from flask import Flask, request, jsonify

app = Flask(__name__)

def trial_division(n):
   factors = [1]
   temp = n
   if n <= 1:
      return [n]

   while n % 2 == 0:
      factors.append(2)
      n //= 2
   p = 3
   while p * p <= n:
      while n % p == 0:
         factors.append(p)
         n //= p
      p += 2
   if n > 1:
      factors.append(n)
   if len(factors) == 2 and factors[1] == temp:
      return [temp]
   return factors

@app.route("/")
def hello():
   return " you called \n"

# curl -d "text=Hello!&param2=value2" -X POST http://localhost:5000/echo
# curl -d "inINT=12" -X POST http://localhost:5000/factors
@app.route("/echo", methods=['POST'])
def echo():
   return "You said: " + request.form['text']

@app.route("/factors", methods=['POST'])
def factors():
   try:
      inINT = int(request.form['inINT'])
   except (KeyError, ValueError):
      return jsonify({"error": "Missing or invalid inINT"}), 400
   result = trial_division(inINT)
   return jsonify(result)

if __name__ == "__main__":
   app.run(host='0.0.0.0')