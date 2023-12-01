import React from "react";
import { useNavigate } from "react-router-dom";
import { Button} from "react-bootstrap";
import "../App.css"


function Leftbar() {
  const navigate = useNavigate()

  const keywords = [
    "ঢাকা",
    "চট্টগ্রাম",
    "রাজশাহী",
    "খুলনা",
    "বরিশাল",
    "সিলেট",
    "ময়মনসিংহ",
    "রংপুর",
  ];
  const division = "division"

  return (
    <div>
      <div className="row custombackground" >
        <h3 className="text-center mt-3 mb-3">Divisions</h3>
      </div>
      <hr />
      <ul className="list-group">
        {keywords.map((keyword, index) => (
          
          <Button
          key={index}
          className="list-group-item btn-sm custombackground"
          style={{  borderRadius: '5px',border: '0.2px solid #2b6777' }}
          onClick={() => {
            navigate("/searchednews", {replace:true, state:{keyword,division}});
          }}
        >
          <span>{keyword}</span>
        </Button>
        ))}
      </ul>
    </div>
  );
}

export default Leftbar;
