import { BrowserRouter, Route, Routes } from "react-router-dom";
import "./App.css";
import HomePage from "./pages/HomePage";
import Page1 from "./pages/Page1";
import LearnMore from "./pages/LearnMore";
import Results from "./pages/Results";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/learnmore" element={<LearnMore />} />
          <Route path="/result" element={<Results />} />
          <Route path="/page1" element={<Page1 />} />
          <Route path="*" element={<div>404</div>} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
