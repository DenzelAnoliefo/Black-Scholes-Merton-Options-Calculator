import { useState } from "react";
import './OptionsPricer.css';

export default function OptionsPricer() {
  const [form, setForm] = useState({
    S: "",
    K: "",
    r: "",
    t: "",
    q: "",
    vol: "",
    operation: "calloption"
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  function handleChange(e) {
    const { name, value } = e.target;
    setForm(prev => ({ ...prev, [name]: value }));
  }

  async function handleSubmit(e) {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const res = await fetch("http://127.0.0.1:8002/calculate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          S: parseFloat(form.S),
          K: parseFloat(form.K),
          r: parseFloat(form.r),
          t: parseFloat(form.t),
          q: parseFloat(form.q),
          vol: parseFloat(form.vol),
          operation: form.operation
        })
      });

      const data = await res.json();

      if (data.error) {
        setError(data.error);
      } else {
        setResult(data.calculation);
      }
    } catch (err) {
      setError("Something went wrong.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div>
      <div className="container">
        <h1>Black‑Scholes Options Pricer</h1>

        <form onSubmit={handleSubmit}>

          <div className="form-group">
            <label>Current stock price ($)</label>
            <input
              name="S"
              value={form.S}
              onChange={handleChange}
              type="number"
              step="any"
              placeholder="e.g. 100"
              required
            />
          </div>

          <div className="form-group">
            <label>Strike price ($)</label>
            <input
              name="K"
              value={form.K}
              onChange={handleChange}
              type="number"
              step="any"
              placeholder="e.g. 105"
              required
            />
          </div>

          <div className="form-group">
            <label>Time to maturity (Yrs)</label>
            <input
              name="t"
              value={form.t}
              onChange={handleChange}
              type="number"
              step="any"
              placeholder="e.g. 0.5"
              required
            />
          </div>

          <div className="form-group">
            <label>Risk‑free interest rate (%)</label>
            <input
              name="r"
              value={form.r}
              onChange={handleChange}
              type="number"
              step="any"
              placeholder="e.g. 5"
              required
            />
          </div>

          <div className="form-group">
            <label>Dividend Yield (%)</label>
            <input
              name="q"
              value={form.q}
              onChange={handleChange}
              type="number"
              step="any"
              placeholder="e.g. 2"
              required
            />
          </div>

          <div className="form-group">
            <label>Volatility (%)</label>
            <input
              name="vol"
              value={form.vol}
              onChange={handleChange}
              type="number"
              step="any"
              placeholder="e.g. 25"
              required
            />
          </div>

          <div className="form-group">
            <label>Operation</label>
            <select
              name="operation"
              value={form.operation}
              onChange={handleChange}
            >
              <option value="calloption">Call Option</option>
              <option value="putoption">Put Option</option>
            </select>
          </div>

          <button type="submit">
            {loading ? "Calculating..." : "Calculate"}
          </button>
        </form>

        {error && <p className="error">{error}</p>}

        {result !== null && (
          <div className="result">
            <span className="label">Result:</span>
            <span className="value">{result}</span>
          </div>
        )}
      </div>

      <div className="footer-tag">Created by Denzel Anoliefo</div>
    </div>
  );
}
